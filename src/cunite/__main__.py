import random

import phub
from nicegui import app, run, ui

from cunite import constants


def get_random_channel(rand, channels):
    return rand.choice(list(channels))


def get_random_video(rand, videos):
    return rand.choice(list(videos))


def ts_notify(label, *args):
    with label:
        ui.notify(*args)


def fetch_video(rand, email, password, useless_label):
    ts_notify(useless_label, "Fetching your Pornhub account...")
    client = phub.Client(email=email, password=password, login=True)
    ts_notify(useless_label, f"Done fetching. Name: {client.account.name}")
    if not client.account:
        ts_notify(
            useless_label, "Operation failed because I counldn't fetch your account."
        )
        return
    if not client.account.subscriptions:
        ts_notify(
            useless_label,
            "Operation failed because I counldn't fetch your subscriptions.",
        )
        return
    ts_notify(useless_label, "Selecting a random channel...")
    selected_channel = get_random_channel(rand, client.account.subscriptions)
    ts_notify(useless_label, f"Selected channel: {selected_channel.name}")
    try:
        ts_notify(useless_label, "Selecting a random video from this channel...")
        selected_video = get_random_video(rand, selected_channel.videos)
        ts_notify(useless_label, f"Selected video: {selected_video.title}")
        ts_notify(useless_label, "Opening the video link...")
    except IndexError:
        ts_notify(useless_label, "Failed to fetch channel or video. Try again.")
        return
    with useless_label:
        ui.navigate.to(selected_video.url, new_tab=True)


async def on_submit(email_inp, password_inp, seed_inp, useless_label):
    email, password, seed = email_inp.value, password_inp.value, seed_inp.value
    for name in ("email", "password"):
        app.storage.user[name] = locals()[name]
    ui.notify("Cached the inputs.")

    rand = random.Random(seed or None)
    await run.io_bound(fetch_video, rand, email, password, useless_label)


@ui.page("/")
def index():
    ui.dark_mode().enable()
    ui.colors(**constants.GRUVBOX_COLORS)

    ui.page_title("Cunite")

    useless_label = ui.label()

    with ui.column(align_items="center", wrap=True).classes("fixed-center"):
        ui.markdown("#**Cunite**").classes("text-positive")
        ui.markdown(
            "Select a random video from a random Pornhub subscription on your account."
        ).style("padding-bottom: 20px")
        with ui.row(align_items="center").classes("justify-center"):
            email = ui.input(placeholder="E-mail").props("rounded outlined dense")
            email.set_value(app.storage.user.get("email"))
            password = ui.input(
                placeholder="Password", password=True, password_toggle_button=True
            ).props("rounded outlined dense")
            password.set_value(app.storage.user.get("password"))
            seed = ui.input(placeholder="Randomization seed").props(
                "rounded outlined dense"
            )

        ui.button(
            "Find a video",
            on_click=lambda: on_submit(email, password, seed, useless_label),
            icon="search",
        ).props("rounded outlined dense").style("margin-top: 40px; padding: 15px")


def main() -> None:
    ui.run(favicon="🌐", reload=constants.RELOAD, storage_secret=constants.STORAGE_SECRET)


main()

import random
import string

from flask import Flask, request, redirect, render_template, abort, make_response

app = Flask(__name__)

link_store = []


def is_code_taken(candidate):
    return any(entry["short_code"] == candidate for entry in link_store)


def make_short_code(size=6):
    alphabet = string.ascii_letters + string.digits
    candidate = "".join(random.choice(alphabet) for _ in range(size))
    while is_code_taken(candidate):
        candidate = "".join(random.choice(alphabet) for _ in range(size))
    return candidate


def normalize_url(raw_url):
    cleaned = raw_url.strip()
    if cleaned and not cleaned.startswith(("http://", "https://")):
        cleaned = "https://" + cleaned
    return cleaned


def find_link(code):
    for entry in link_store:
        if entry["short_code"] == code:
            return entry
    return None


@app.route("/<code>")
def go_to_target(code):
    entry = find_link(code)

    if entry is None:
        abort(404)

    entry["clicks"] += 1

    resp = make_response(redirect(entry["original_url"]))
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return resp


@app.route("/", methods=["GET", "POST"])
def home():
    new_short_url = None

    if request.method == "POST":
        submitted_url = normalize_url(request.form.get("url", ""))

        if submitted_url:
            new_code = make_short_code()
            link_store.insert(0, {
                "short_code": new_code,
                "original_url": submitted_url,
                "clicks": 0,
            })
            new_short_url = request.host_url + new_code

    return render_template("index.html", short_url=new_short_url, links=link_store)


if __name__ == "__main__":
    app.run(debug=True)
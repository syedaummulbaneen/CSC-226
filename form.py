from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
  <body>
    <h2>Submit a Message</h2>
    <form method="POST" action="/submit">
      Name: <input type="email" name="name"><br><br>
      Message: <input type="text" name="message"><br><br>
      <input type="submit" value="Submit">
    </form>
    <p>See all messages at <a href="/messages">/messages</a></p>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(form_html)

@app.route("/submit", methods=["POST"])
def submit():
    # Get form data from request.form
    name = request.form.get("name")
    message = request.form.get("message")

    # Save it to a file (append mode - make sure you are appending to the file, not overwriting the whole thing)
    with open("messages.txt", "a") as file:
        file.write(f"Name: {name}\nMessage: {message}\n\n")

    return redirect("/messages")

@app.route("/messages", methods=["GET"])
def messages():
    # Read file content and return as plain text or HTML
    with open("messages.txt", "r") as file:
        content = file.read()

    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(debug=True)

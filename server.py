"""
    Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detect():
    """
    This function handles requests to the "/emotionDetector" endpoint, 
    retrieves the text from the request arguments, and calls the 
    `emotion_detector` function to analyze the emotions in the text.

    The response includes:
    - A breakdown of detected emotions (formatted as a string).
    - The dominant emotion in the text.

    Returns:
        str: A formatted response describing detected emotions and 
             the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion and remove it from the dictionary
    dominant_emotion = response.pop("dominant_emotion")

    # If the dominant emotion is None, then return a message
    if not dominant_emotion:
        return "Invalid text! Please try again!"

    # convert the json object to a string, remove the brackets and replace the double
    # quotes with single quotes, and insert the word and before 'sadness'
    response_str = json.dumps(response)
    response_str = response_str.replace("{", "").replace("}", "")
    response_str = response_str.replace('"', "'").replace(", 'sad", " and 'sad")

    # Add the descriptive text to the formatted output
    response_str = f"For the given statement, the system response is {response_str}."
    response_str = f"{response_str} The dominant emotion is {dominant_emotion}."

    # return the formatted text
    return response_str


@app.route("/")
def render_index_page():
    """
    Renders the index page.

    This function handles requests to the root URL ("/") and returns 
    the rendered 'index.html' template.

    Returns:
        Response: The rendered HTML content of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

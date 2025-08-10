##Importing Libs
import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown


##Setting up Model
API_KEY = "Your API"
genai.configure(api_key= API_KEY),
model = genai.GenerativeModel("gemini-2.5-flash")

##The Layout
topic_input = widgets.Text(
    description = "TOPIC",
    layout = widgets.widgets.Layout( width = "400px"))

tone_input = widgets.Dropdown(
    description = "TONE",
    options = ['witty', 'casual', 'normal', 'professional', 'angry', 'sarcastic'],
    layout = widgets.widgets.Layout( width = "400px")
)

audience_input = widgets.Text(
    description = "AUDIENCE",
    layout = widgets.widgets.Layout( width = "400px")
)

hastag_input = widgets.Text(
    description = "HASHTAGS",
    layout = widgets.widgets.Layout( width = "400px")
)

submit_button = widgets.Button(
    description = "Generate Tweet",
    button_style = 'Success',
    tooltip = 'click to generate tweet',
    layout = widgets.Layout( width = "400px")
)

output = widgets.Output()

##Defining Prompt and Generating a response
def generate_tweet(b):
  output.clear_output()
  prompt = f"""
      You are an expert Content writer.
      Generate a tweet about the topic - {topic_input.value}.
      use a ton {tone_input.value}.
      generate tweet for audience {audience_input.value}.
      also include the hashtag {hastag_input.value}.
      Keep it under 100 words.
  """

  with output:
    try:
      response = model.generate_content(prompt)
      tweet = response.text.strip()
      display(Markdown(f"## Generated Tweet: \n\n{tweet}"))
    except Exception as e:
      print("Error: ", e)

submit_button.on_click(generate_tweet)


##Creating the form and displaying
form = widgets.VBox([
    widgets.HTML(value= "<h3>Agent to Generate Tweet </h3>"),
    topic_input,
    tone_input,
    audience_input,
    hastag_input,
    submit_button,
    output
])

display(form)

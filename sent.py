# import spacy
# from textblob import TextBlob
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# # Initialize VADER sentiment analyzer
# vader_analyzer = SentimentIntensityAnalyzer()

# female_terms = {'she', 'her', 'hers', 'woman', 'women', 'girl', 'girls', 'female', 'mother', 'daughter', 'sister', 'aunt', 'niece'}
# male_terms = {'he', 'him', 'his', 'man', 'men', 'boy', 'boys', 'male', 'father', 'son', 'brother', 'uncle', 'nephew'}

# def analyze_text(text):
#     # Process the text with spaCy
#     doc = nlp(text)
    
#     # Count gendered terms
#     female_count = sum(1 for token in doc if token.text.lower() in female_terms)
#     male_count = sum(1 for token in doc if token.text.lower() in male_terms)
    
#     # Extract named entities
#     female_entities = [ent.text for ent in doc.ents if ent.label_ == 'PERSON' and any(token.text.lower() in female_terms for token in ent)]
#     male_entities = [ent.text for ent in doc.ents if ent.label_ == 'PERSON' and any(token.text.lower() in male_terms for token in ent)]
    
#     # Sentiment analysis using TextBlob
#     blob = TextBlob(text)
#     textblob_sentiment = blob.sentiment
    
#     # Sentiment analysis using VADER
#     vader_sentiment = vader_analyzer.polarity_scores(text)
    
#     return {
#         'female_count': female_count,
#         'male_count': male_count,
#         'female_entities': female_entities,
#         'male_entities': male_entities,
#         'textblob_sentiment': textblob_sentiment,
#         'vader_sentiment': vader_sentiment
#     }

# def identify_gender_bias(analysis):
#     female_count = analysis['female_count']
#     male_count = analysis['male_count']
#     textblob_sentiment = analysis['textblob_sentiment']
#     vader_sentiment = analysis['vader_sentiment']
#     female_entities = analysis['female_entities']
#     male_entities = analysis['male_entities']
    
#     bias_summary = {
#         'gender_bias': None,
#         'female_mentions': female_count,
#         'male_mentions': male_count,
#         'female_entities': female_entities,
#         'male_entities': male_entities,
#         'textblob_sentiment': textblob_sentiment,
#         'vader_sentiment': vader_sentiment,
#         'textblob_sentiment_towards_female': None,
#         'textblob_sentiment_towards_male': None,
#         'vader_sentiment_towards_female': None,
#         'vader_sentiment_towards_male': None
#     }
    
#     # Determine gender bias based on mentions
#     if female_count > male_count:
#         bias_summary['gender_bias'] = 'Female'
#     elif male_count > female_count:
#         bias_summary['gender_bias'] = 'Male'
#     else:
#         bias_summary['gender_bias'] = 'Neutral'
    
#     # Detailed sentiment evaluation logic
#     if textblob_sentiment.polarity > 0:
#         if female_count > 0:
#             bias_summary['textblob_sentiment_towards_female'] = 'Positive'
#         if male_count > 0:
#             bias_summary['textblob_sentiment_towards_male'] = 'Positive'
#     elif textblob_sentiment.polarity < 0:
#         if female_count > 0:
#             bias_summary['textblob_sentiment_towards_female'] = 'Negative'
#         if male_count > 0:
#             bias_summary['textblob_sentiment_towards_male'] = 'Negative'
    
#     if vader_sentiment['compound'] > 0:
#         if female_count > 0:
#             bias_summary['vader_sentiment_towards_female'] = 'Positive'
#         if male_count > 0:
#             bias_summary['vader_sentiment_towards_male'] = 'Positive'
#     elif vader_sentiment['compound'] < 0:
#         if female_count > 0:
#             bias_summary['vader_sentiment_towards_female'] = 'Negative'
#         if male_count > 0:
#             bias_summary['vader_sentiment_towards_male'] = 'Negative'
    
#     return bias_summary

# def is_text_biased(gender_bias_data):
#     female_mentions = gender_bias_data['female_mentions']
#     male_mentions = gender_bias_data['male_mentions']
#     textblob_sentiment_towards_female = gender_bias_data['textblob_sentiment_towards_female']
#     textblob_sentiment_towards_male = gender_bias_data['textblob_sentiment_towards_male']
#     vader_sentiment_towards_female = gender_bias_data['vader_sentiment_towards_female']
#     vader_sentiment_towards_male = gender_bias_data['vader_sentiment_towards_male']
    
#     # Determine mention bias
#     mention_bias = None
#     if female_mentions > male_mentions:
#         mention_bias = 'Female'
#     elif male_mentions > female_mentions:
#         mention_bias = 'Male'
    
#     # Determine sentiment bias
#     sentiment_bias = None
#     if (textblob_sentiment_towards_female == 'Positive' and textblob_sentiment_towards_male != 'Positive') or (vader_sentiment_towards_female == 'Positive' and vader_sentiment_towards_male != 'Positive'):
#         sentiment_bias = 'Female'
#     elif (textblob_sentiment_towards_male == 'Positive' and textblob_sentiment_towards_female != 'Positive') or (vader_sentiment_towards_male == 'Positive' and vader_sentiment_towards_female != 'Positive'):
#         sentiment_bias = 'Male'
    
#     # Determine overall bias
#     overall_bias = 'Neutral'
#     if mention_bias == sentiment_bias and mention_bias is not None:
#         overall_bias = mention_bias
#     elif mention_bias is not None and sentiment_bias is not None and mention_bias != sentiment_bias:
#         overall_bias = 'Mixed'
    
#     return overall_bias

# # Example text
# # text = """
# #     She is an excellent manager. she is a strong leader.
# #     Her performance was outstanding. Her work was remarkable.
# #     The girls in the team showed great skill. The boys were very dedicated.
# #     Mary was praised for her efforts, while John was criticized.
# # """

# analysis = analyze_text(text)
# gender_bias = identify_gender_bias(analysis)
# result = is_text_biased(gender_bias)
# print(result)









import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyDR3z9bQuZBbRkY6wJLBgdW3nx2T5VekQs")
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash")
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Analyze the sentiment of the following Tweets and classify them as biased,unbaised, or nutral and return baised sentences. \"she is a beautiful girl\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "unbaised",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"men are much stronger than female,female played well\"",
      ],
    },
    {
      "role": "model",
      "parts": {
        "biased",
      },
    },
    {
      "role": "user",
      "parts": [
        "\"it's a game between men and women,women won that game as they performed well.\"",
      ],
    },
    {
      "role": "model",
      "parts": {
        "nutral",
      },
    },
  ]
)
st.title("bias detection")
text=st.text_input("enter the file")
button=st.button("submit")
if button:
    response = chat_session.send_message(text)
    st.write(response.text)
# The fireman and the policeman helped the stewardess.Mankind has always relied on manpower. The congressman gave a speech.

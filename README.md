# Sentiment-analyser

The program for sentiment analysis of text content.

Input data are a text content, and a language of the text content ("ukr", "rus" and "eng").
The limit of prediction is 0.9.

Output data is "Good" or "Bad" label that describe a emotion of input text content.

"eng_infostream_v2.ftz" is model trained on 300000 infostream messages that have "__label__pos" or "__label__neg" label (labels obtained as result of dictionary-based classification (Lande algorithm)).

"rus_infostream.ftz" is model trained on 260000 messages that have "__label__pos" or "__label__neg" label (labels obtained as result of dictionary-based classification (Lande algorithm)).

"ukr_infostream_v2.ftz" is model trained on 260000 messages that have "__label__pos" or "__label__neg" label (labels obtained as result of dictionary-based classification (Lande algorithm)).
# Sentiment-analyser

**The program for sentiment analysis of text content.**

*Input data* are a text content, and a language of the text content (`ukr`, `rus` and `eng`).
By default, the limit of prediction is 0.9.

*Output data* is `Good` or `Bad` label that describe a emotion of input text content.
In the case of an unexpectable language or a prediction is lower than 0.9 output data is `None`.

## Models

The program uses three pre-trained models ([**ukr_infostream_v2.ftz**](https://drive.google.com/file/d/1njXnzZF6A7Zv4BELJdgDE0cwZHZgQwtZ/view?usp=sharing), [**rus_infostream.ftz**](https://drive.google.com/file/d/1dW-3eyDXQvS4PFx9uPI9bXs7metFVsZ4/view?usp=sharing) and [**eng_infostream_v2.ftz**](https://drive.google.com/file/d/1ugBnDWHrzZV7AmejnS-OPoiGqrhy53Zn/view?usp=sharing) for Ukrainian, Russian and English language, accordingly) that ontained with applying an open-source Python library [FastText](https://fasttext.cc/).

In order to train a text classifier using the [FastText](https://fasttext.cc/), the `fasttext.train_supervised` function with the following hyperparameters was used:

		hyper_params = { 
			"lr": 0.35,         # Learning rate
			"epoch": 100,       # Number of training epochs to train for
			"wordNgrams": 3,    # Number of word n-grams to consider during training
			"dim": 155,         # Size of word vectors
			"ws": 5,            # Size of the context window for CBOW or skip-gram
			"minn": 3,          # Min length of char ngram
			"maxn": 20,          # Max length of char ngram
			"bucket": 2014846,  # Number of buckets
			}
		
A  text file `traindata_lang.txt` contained a training sentence per line along with the labels prefixed by the string `__label__` (`__label__pos` or `__label__neg`) were used.

In order to compress and have a much smaller model file and, as a result, reduce space usage, obtained models were quantized and saved in `.ftz` format.
To quantize and compress model, the `quantize` function with the following parameters was used:

		model.quantize(
			input=None,
			qout=False,
			cutoff=0,
			retrain=False,
			epoch=None,
			lr=None,
			thread=None,
			verbose=None,
			dsub=2,
			qnorm=False,
			)

- [**ukr_infostream_v2.ftz**](https://drive.google.com/file/d/1njXnzZF6A7Zv4BELJdgDE0cwZHZgQwtZ/view?usp=sharing) is model trained on the `traindata_ukr.txt` containing 260000 Ukrainian messages per line along with the `__label__pos` or `__label__neg` labels.
- [**rus_infostream.ftz**](https://drive.google.com/file/d/1dW-3eyDXQvS4PFx9uPI9bXs7metFVsZ4/view?usp=sharing) is model trained on the `traindata_rus.txt` containing 260000 Russian messages per line along with the `__label__pos` or `__label__neg` labels.
- [**eng_infostream_v2.ftz**](https://drive.google.com/file/d/1ugBnDWHrzZV7AmejnS-OPoiGqrhy53Zn/view?usp=sharing) is model trained on the `traindata_eng.txt` containing 300000 English messages per line along with the `__label__pos` or `__label__neg` labels.

The pre-labeled messages were obtained with the help of the news monitoring system - [InfoStream](http://infostream.ua/ENG/).
Labels of these messages obtained as result of [dictionary-based classification](https://arxiv.org/abs/0806.2738).
To collect the training data, the messages with extremely high emotional weights were selected. 

## Requirements
To run the `sentiment_analyzer.py` script you will need:
- python 3.8 or newer
- to install [fastText-0.9.2](https://pypi.org/project/fasttext/)
- to create the folder `Models` in the root folder, download and unpack there pre-trained models [**ukr_infostream_v2.ftz**](https://drive.google.com/file/d/1njXnzZF6A7Zv4BELJdgDE0cwZHZgQwtZ/view?usp=sharing), [**rus_infostream.ftz**](https://drive.google.com/file/d/1dW-3eyDXQvS4PFx9uPI9bXs7metFVsZ4/view?usp=sharing) and [**eng_infostream_v2.ftz**](https://drive.google.com/file/d/1ugBnDWHrzZV7AmejnS-OPoiGqrhy53Zn/view?usp=sharing) for Ukrainian, Russian and English language, accordingly

## Copyright
Copyright © 2021 [Dmytro Lande](http://dwl.kiev.ua/), [Oleh Dmytrenko](http://odmytrenko.tilda.ws/)

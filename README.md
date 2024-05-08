# Peanut Shell

`Peanut Shell` is a reranking service for better RAG performance. The underlying model used is [cross-encoder/ms-marco-MiniLM-L-6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2).

## User Guide

It's recommended to run `Peanut Shell` as a docker container.

### How to install

Use the commands below to clone this repo and run the docker container.

```shell
$ git clone git@github.com:sugarforever/peanut-shell.git
$ cd peanut-shell
$ docker compose up -d
```

### How to use

The only API exposed is. Refer to the example below on how to make API call.

```shell
curl --location 'http://localhost:8000/v1/rerank/' \
--header 'Content-Type: application/json' \
--data '{
    "query": "What is the capital of the United States?",
    "top_n": 3,
    "documents": [
        "Carson City is the capital city of the American state of Nevada.",
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
        "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
        "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states."
    ]
}'
```

You should expect similar response as below:

```json
{
    "results": [
        {
            "index": 2,
            "relevance_score": 8.186723709106445
        },
        {
            "index": 3,
            "relevance_score": 0.2271757274866104
        },
        {
            "index": 0,
            "relevance_score": -2.0371546745300293
        }
    ]
}
```
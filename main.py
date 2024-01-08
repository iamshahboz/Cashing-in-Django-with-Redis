from fastapi import FastAPI, HTTPException
from enum import Enum 

app = FastAPI()

# don't forget to add type hints


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'

BANDS = [
    {'id':1, 'name': 'The kinks', 'genre': 'Rock'},
    {'id':2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id':3, 'name': 'Slowdive', 'genre': 'Shoegaze'},
    {'id':4, 'name': 'Wu Tang Chan', 'genre': 'Hip-Hop'},
]


@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{band_id}')
async def bands(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    return band 

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]



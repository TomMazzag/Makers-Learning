# {{ /albums }} Route Design Recipe

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

## 1. Design the Route Signature
```
# albums route
POST /albums
  title: string
  release_year: int
  artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /albums
#  Parameters:
#    title: Voyage
#    release_year: 2022 
#    artist_id: 2
#  Expected response (200 OK):
"""
(No content)
"""
```

## 3. Test-drive the Route

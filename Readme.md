Here's the text with correct indentation and formatting:

---

This will create a Docker container that runs a Flask API and builds Prometheus metrics based on the number of times the API is called.

## Instructions

### From Local Machine

1. Run: `docker-compose build`
2. Run: `docker-compose up`
3. Call `http://localhost:5001/` **OR** run `test.py` (assertion test) a random number of times.
4. Check `http://localhost:9090/`:
   - a. Search for the metric `api_calls_total`, then hit "Execute".
   - b. Verify that the number matches the number of times `http://localhost:5001/` was called.
   - c. Hit `http://localhost:5001/` X more times and verify that `http://localhost:9090/` increments the counter.

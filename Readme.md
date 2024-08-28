This will create a docker container that creates a flask API and builds prometheus metrics based on the number of times that the API is called

## instructions 

From local machine
1 Run: docker-compose build
2 Run: docker-compose up 
3 Call http://localhost:5001/ OR run test.py(assertion test) a random number of times
4 Check http://localhost:9090/
    a. Search for metric 'api_calls_total', hit execute
    b. Verify number is the same as the number of times http://localhost:5001/  was called
    c. Hit http://localhost:5001/  X more times and verify http://localhost:9090/ increments the counter

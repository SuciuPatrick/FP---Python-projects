from test.clientTest import callTestClient
from test.movieTest import callTestMovie
from test.testRepo import callRepoTest

def runTests():

	callTestClient()
	callTestMovie()
	callRepoTest()

def prepareAjaxErrorMessage(message):
	return {'success':0, 'message':message}

def prepareAjaxSuccessData(result, dataLength):
	return {'success':1, 'result':result, 'length':dataLength}
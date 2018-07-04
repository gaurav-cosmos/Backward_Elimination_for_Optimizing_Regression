def(X_train,X_test,SLM=0.05):
	import numpy as np
	import statsmodels.formula.api as sm

	X_opt = X_train[:,:].copy()
	
	"""BACKWARD SELECTION"""
	i=0
	while 1:
		print("fitting to X_opt")    
		regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
		P = (regressor_OLS.pvalues)
		adjR_before = regressor_OLS.rsquared_adj.astype(float)
		max_P = np.argmax(P)
		adjR = adjR_before.copy()
		X_tmp_opt = np.delete(X_opt, max_P, 1)

		print("#fitting to new tmp opt")    
		regressor_OLS_tmp = sm.OLS(endog = y, exog=X_tmp_opt).fit()
		adjR_after = regressor_OLS_tmp.rsquared_adj.astype(float)

		print("checking for R-square condition")
		if(adjR>=0.90):
		    if(adjR_before>adjR_after):
		        print(i + "). Removed feature with Chi-Squared-"+max_P)
		        i+=1
		        break
		    else:
		        X_opt = X_tmp_opt
		        X_test = np.delete(X_test, max_P, 1)
				print(i + "). Removed feature with Chi-Squared-"+max_P)
		        i+=1
		else:
		    X_opt = X_tmp_opt
		    X_test = np.delete(X_test, max_P, 1)
		    print(i + "). Didn't remove any feature")
		    i+=1
	
	return X_opt,X_test
	

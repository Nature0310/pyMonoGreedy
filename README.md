# pyMonoGreedy
Bigeye structure optimization

Branch:

* master:public version
* dev:develop

git:

* git clone
* git branch
* git checkout <name>
* git checkout -b dev origin/dev
* git add 
* git commit -m " "
* git push origin dev
* git branch --set-upstrea dev origin/dev
* git pull
* git merge <name>
* git branch -d <name>

## Readme
### setup

### coding structure

		init() # include each init() declare object

		InputOutput:  hu
    		data:
             	int phi_min
             	int phi_max
      	  		double budget 
            
             	other parameters
   		function:
   				init()
             	get_config() # prototxt input 
		  		save_output()  # prototxt output 
		  
		  

		EncoderDecoder:  hu 
			var:
				phi
				set_phi
           		phi_step
           		phi_offset_max_float  
			functions:
           		init()
				linear_encoding() # encoding
   				linear_decoding() 



		EvaluatePhi:  hu
      		var:
           		eva_times_upperbound = 2
           		eva_history # 

      		function:
             	get_p_and_t(phi)
             	add_phi_to_history(phi)
             	eva_p_and_t(phi)  # real evaluation  
             	get_best_phi() # budget


		Optimization:  jin
       		var:

       		function:      


		FunctionTransform:  jin
       		var:

       		function:


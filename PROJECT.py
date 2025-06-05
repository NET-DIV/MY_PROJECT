from flask import Flask, request, jsonify, render_template, render_template_string


app = Flask(__name__)
@app.route("/")
def html():
	with app.app_context():
		html = '''<!DOCTYPE html>
				      <html>
    		 		 <head>
        		 	 	<title> HELLO THERE </title>
         			 </head>
    		 		 <body> 
    				  	<bgcolor="black">
    			 	 	<h1>
        			  	<ul>HELLO THERE</ul>
        			  	<ul>HOW DID YOU GET HERE</ul>
        			  	<p> TklHR0VS </p>
        			  	<p> Decode it</p> 
    			  </body> 
				  </html>'''
		return render_template_string(html)
		
		
if __name__ == '__main__':
	app.run("127.0.0.1", 5050, debug=True)
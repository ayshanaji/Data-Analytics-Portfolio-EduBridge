
# <div align="center"><u><b>Passenger Satisfaction-Classification Models</b><u></div>
####         - Build a model to predict the satisfaction of Passenger
![image](https://user-images.githubusercontent.com/99160088/170905381-d9bc0d88-d20b-4e8c-832b-086749ead414.png)

### <u>Overview<u>:

#### What is Airline Paseenger Satisfaction?
The airline passenger satisfaction survey is an in-depth feedback questionnaire that an airline sends to its passenger to collect feedback about the flying experience.This sample survey template helps collect data on a macro and micro level from all the passengers on each flight to monitor service quality and collect feedback about any deterioration of services. These survey questions can be tweaked to collect data about each aspect of a flight experience and manage services and training according to the customers expectations, wants and likes.

### <u>Dataset<u>:

    https://www.kaggle.com/code/wenchilin/passenger-satisfaction-classification-models
    
### <u>Dataset details<u>


<table>
  <tr>
    <th>Field</th>
    <th>Description</th>
  
  </tr>
  <tr>
    <td><u>ID<u></td>
    <td>Unique passenger identifier</td>
  </tr>
     <tr>
    <td><u>Gender<u></td>
    <td>Gender of the passenger (Female/Male)<u></td>
  </tr>
   <tr>
    <td><u>Age<u></td>
    <td>Age of the passenger</td>
  </tr>
        <tr>
    <td><u>Customer Type<u></td>
    <td>Type of airline customer (First-time/Returning)</td>
  </tr>
        <tr>
    <td><u>Type of Travel<u></td>
    <td>Purpose of the flight (Business/Personal)</td>
  </tr>
         <tr>
    <td><u>Class<u></td>
    <td>Travel class in the airplane for the passenger seat</td>
  </tr>
         <tr>
    <td><u>Flight Distance<u></td>
    <td>	Flight distance in miles</td>
  </tr>
        <tr>
    <td><u>Departure Delay<u></td>
    <td>Flight departure delay in minutes</td>
  </tr>
         <tr>
    <td><u>Arrival Delay<u></td>
    <td> Flight arrival delay in minutes</td>
  </tr>
        <tr>
    <td><u>Departure and 
            Arrival Time Convenience	<u></td>
    <td> Satisfaction level with the convenience of the flight departure and arrival times 
                         </td>
  </tr>
        <tr>
    <td><u>Ease of Online Booking	    <u></td>
    <td> Satisfaction level with the online booking experience 
                            </td>
  </tr>
         <tr>
    <td><u>Check-in Service<u></td>
    <td> Satisfaction level with the check-in service </td>
  </tr>
        <tr>
    <td><u>Online Boarding	  <u></td>
    <td> Satisfaction level with the online boarding experience</td>
  </tr>
        <tr>
    <td><u>Gate Location<u></td>
    <td> Satisfaction level with the gate location in the airport </td>
  </tr>
        <tr>
    <td><u>On-board Service<u></td>
    <td> Satisfaction level with the on-boarding service in the airport </td>
  </tr>
        <tr>
    <td><u>   Seat Comfort<u></td>
        <td> Satisfaction level with the comfort of the airplane seat </td>
  </tr>
        <tr>
    <td><u>Leg Room Service<u></td>
    <td> Satisfaction level with the leg room of the airplane seat </td>
  </tr>
        <tr>
    <td><u>Cleanliness<u></td>
    <td>  Satisfaction level with the cleanliness of the airplane </td>
  </tr>
         <tr>
    <td><u>Food and Drink<u></td>
    <td>  Satisfaction level with the food and drinks on the airplane  </td>
  </tr>
         <tr>
    <td><u>In-flight Service<u></td>
    <td>   Satisfaction level with the in-flight service</td>
  </tr>
         <tr>
    <td><u>In-flight Wifi Service<u></td>
    <td>   Satisfaction level with the in-flight Wifi service </td>
  </tr>
         <tr>
    <td><u>In-flight Entertainment<u></td>
    <td>  Satisfaction level with the in-flight entertainment </td>
  </tr>
        <tr>
    <td><u>Baggage Handling<u></td>
    <td>  Satisfaction level with the baggage handling </td>
  </tr>
        <tr>
    <td><u>Satisfaction<u></td>
    <td>  Overall satisfaction level with the airline 
                            (Satisfied/Neutral or unsatisfied) </td>
  </tr>

</table>


        
### <u>Problem Statement:<u>
 <b>Satisfaction</b> is a consumer's subjective evaluation of the extent to which desires and demands arising from
acquiring or consuming a provided product orservice are satisfied, and reusability isthe possibility that the customer
will continue to use the product or service repeatedly after purchasing.

Airline customer satisfaction prediction model implementation, and performance evaluation are conducted with pre-processing.
        
#### The objective is to predict the satisfaction level for customer according to certain criterias. 
        
        
### <u>Implementation:<u>

<u>**Libraries:**<u> 
    `NumPy`  `pandas` `sklearn`  `Matplotlib`  `Seaborn`
              
### <u>Approach:<u>       
  The aim is to create a model that helps the users to apply machine learning approach to predict the satisfaction level. Here, the models used are 

* Logistic Regression
* Naive Bayes
* KNN
* Decision Tree
* Random Forest
* AdaBoost
        
### <u>Conclusion:<u>

* In the first view,the satisfaction level was lower than 50%
# <div align="center"><u><b>Satisfaction level </b><u></div>
# <div align="center"> ![image](https://user-images.githubusercontent.com/99160088/170905450-34fa9be0-f10c-400e-aff6-b8a761b82081.png)</div>

    
* Then Model was created to predict the satisfaction level on the basis of certain criterias which would help Aviation department to improve the facilities for the travellers
### <u>Comparison all Models:<u>

<table>
 <tr>
   <th>Model</th>
   <th>Accuracy Percentage</th>
   <th>ROC-AUC</th>
   <th>Timetaken</th>
  
 </tr>
 <tr>
   <td><u>Logistic Regression<u></td>
   <td>80%</td>
   <td>0.79</td>
   <td>1.13</td>
 </tr>
 </tr>
  <tr>
    <td><u>Decision Tree Classifier<u></td>
    <td>94%</td>
    <td>0.94</td>
    <td>0.52</td>
  </tr>
        </tr>
  <tr>
    <td><u>Random Forest<u></td>
    <td>96%</td>
    <td>0.95</td>
    <td>8.95</td>>
  </tr>
        <tr>
    <td><u>Naive Bayes<u></td>
        <td>86%</td>
        <td>0.86</td>
        <td>0.09</td>
  </tr>
         <tr>
    <td><u>KNN<u></td>
    <td>78%</td>
    <td>0.77</td>
    <td>12O.32</td>
  </tr>
        <tr>
    <td><u>ADA Boost<u></td>
    <td>92%</td>
    <td>0.92</td>
    <td>4.18</td>
  </tr>

</table>

##### For a best model for prediction 
* Maximum ROC_AUC curve
* Minimum time is required 
##### Comparing **Random Forest** is the best from among the models trained to predict the accurate result with an **accuracy** of **96%** and **time taken** to execute is **8.95**
      

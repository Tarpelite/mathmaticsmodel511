## statues for the cells:
 0 for the road  
 1 for tne passenger  
 2 for the cargo  
 3 for the building-1  
 4 for the building-2  
 5 for the building-3  

 ## Transformation Principles
 1.road have the possiblity `p1` to have passenergers stepped on(`0->1`) when there're passengers around, but after a certain period `T1` the passengers will leave (`1->0`)    
 2.passenger have a possibility p1 to move to a road area around. Every time, the passengers will have a possibility `p2` to step onto the road around the building.(`0->1`)  
 3.Cargo have a tendency to follow the passengers (considering the cargo get to the target owner and move with its owner together) while still have a possibility `p3` to stick to the resporisty(or you mean gathering-stall).  
 4.building-1 refers to the buildings like dormitary which have the most people out in the morning.    
 5.building-2 refers to the buildings like canteen which have the most people out after each meals(lunchtime and dinner time particularly)  
 6.building-3 refers to the buildings like teaching-building and office-building which have the most people out in the evening.  


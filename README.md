# InternationalSpaceStation
A newer version to include cloud cover

Thank you for checking out this project. This was originally a bootcamp solo project. I have since remade it with a couple new twists to create a little more utility. I will eventually turn this into a desktop app so that the user can input their location. For now, My location is hard coded into the project. If you see any errors, please feel free to make a request to change the code. I am happy for any and all support. 

This project pulls from 3 different APIs, though I could have used two. I like using a variety of sources which is why I am using the APIs I am using. Obviously the most important was from NASA's ISS API that pinpoints the exact location based on LAT/LONG. The sunrise/sunset API is another original key component as dark hours are required to see the ISS if and when it crosses overhead. Finally, I chose to add a weather API to provide data on the cloud coverage. None of the other data points are even relavent if there is a heavy enough cloud cover to block all view. I set the cloud cover percentage to 40%. This may still be too excessive when it comes to good visability. I will continue to test to find what the best IRL percentage would be for optimal viewing. 

The ISS must be within 5 degrees of the users current LAT/LONG for the program to trigger the next query. If it is between sunset and sunrise the final search will be triggered and if the cloud coverage is less than 40% the IMTPLib will send an email to the user stating they can go outside and look up. 

##NOTE##
What happens if the cloud cover is exactly 40% will this be an error? This is a good place for someone to collaborate with this project and request a change. 

An email can be subbed out for a text message. Twillio is a great option for this change. I use email as the program would also continuously run for the usual 5 minute intervals to one minute intervals as long as all three of the statements remain true. 

This has been a fun little project and I am looking forward to making it into something much easier to modify and allow for other people to use without access of python or an IDE.

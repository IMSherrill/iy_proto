InterestYou is an application to help you keep in touch with your friends and colleagues.

My web application, currently nicknamed InterestYou, is a useful tool to help users keep in touch or renew 
relationships with friends and colleagues. Interaction with the application is simple: the user is prompted to 
enter a set of contacts, along with a few keywords that relate to interesting topics you’ve discussed with each 
person. The application then updates you (the user) by e-mail when there are new magazine or news articles that 
relate to your contacts’ topics of interest, giving you the option to e-mail the article link to that person with
your own message.

InterestYou’s backend is written in a server-side language called Python and uses the Django framework to serve 
pages and interact with the storage layer, a MySQL database. The application gathers the articles using a news 
aggregation API (application programming interface - a method of connecting to external systems) called Daylife. 

In order to store all the necessary information to run the program, I had to create a number of models 
(objects contained in database tables). The Contact model stores the name of the contacts, which user the 
contact belongs to, a list of search terms for the contact, the articles that are related to that contact, 
and whether the user wants to be emailed about this contact. The SearchTerm model stores a list of articles 
related to that search term, and (most importantly) the keywords that the user inputs. The Article model 
stores the headline of the article, the url of the article, the publication source and date, and a blurb 
about the article. 

The last model, called Suggestion, is a model that defines the relationship between a contact and an article. 
This is helpful because a single contact can have many articles, and a single article can belong to many different 
contacts, so a model is required to capture a unique combination of Contact and Article (for example: 
“you should send Jim this NYT article”). This model keeps track of whether a Suggestion has already been made in 
order to prevent the system from repeatedly suggesting the same followup, and is the unit that’s displayed to the 
user.

Thanks for taking a look!

import pyttsx3
engine = pyttsx3.init()
engine.say("""

Art of Data Problem Solving

Class Notes 
cs145
Shiva
Fall, 2023 and 2024


Introduction
We live in an exciting post-GPT era, where getting code snippets or definitions for specific subproblems is a breeze! But while these "atomic" snippets are great, they're like tiny pieces of a larger puzzle.  Don't worry though, we've got you covered. We'll show you how to connect the dots and master the art of assembling the jigsaw puzzle of data systems. So get ready to solve some real-world data problems and unleash your inner data wizard!
Let's explore how to create a consumer data app like Spotify. It's not just about coding to process data; it’s about building the app to scale to millions of consumers, making it fast for users, making it easy for engineers and designers to add and modify  new features as user behaviors evolve. For these, we need to connect different concepts like SQL databases, data models, key-value stores, and data privacy. And to make a fast app, we need a good grasp of query optimization, row and column stores, sorting, hashing, and indexing. It's like putting together a puzzle, and each piece is essential to create the big picture and a compelling data app for users.
We have curated a few case studies and companion python/SQL notebooks on specific topics.  From these examples, you will learn key principles on how to 
Applications: Build a streaming service like Spotify storing playlists, songs, and lyrics using SQL databases and key-value stores, both in the cloud and on your phones. Explore data privacy and ethics through Google's COVID mobility reports, and learn how they protect user privacy.
Storage & Indexing Techniques: Speed up your Spotify queries with row and column  stores, sorting, hashing, and indexing. See how OpenAI's GPT and Google Maps handle complex data types like text and geographical data using embeddings, hashing, and indexing using vector databases. See how to build incremental updates.  
Transactional Data Structures & Concurrency Theory: Dig into Ticketmaster's challenges when selling Taylor Swift concert tickets to millions of eager fans. Explore ACID properties to ensure fans are not double sold the same tickets, and are guaranteed tickets once they pay for them. Learn how to build a basic transaction system using parallel programming, locking, and logging techniques.  
Big Data Systems: Learn how Discord scaled from storing billions to trillions of messages in five years. Follow how Google Ads evolved from ten MySQL databases in 2003 to a SQL-based Spanner system in 2023, handling hundreds of billions of dollars in transactions each year. Understand how to design and manage complex data systems that can scale effectively. Learn how to partition data and computation so analysis and AI systems can work with Terabytes to Petabytes to build training and inference systems. Learn how applying lessons from distributed systems, pub-sub, message queues, and tools like Kafka can help decouple problems like ticket scalping and bot attacks.
Notebooks: We offer five interactive Colabs to enhance your learning experience. 
Build a Spotify-like service using SQL. 
NanoDB is a simple toy database designed to teach storage concepts (~100 lines of python), indexing techniques (~200 lines), and join algorithms (~300 lines). 
Hashing algorithms (~300 lines), for working with high-dimensional text embeddings (e.g, from OpenAI), geo data (e.g., from Uber) and image data.
Concert Transactions notebook, on how to construct a Ticketmaster example (~200 lines), build a basic Transactions system (~250 lines), and explore concepts like concurrent transactions, parallel programming, and locking (~200 lines) and logging algorithms.
Distributed Systems, on how to use MessageQueues in a cluster of machines (~150 lines), and how to store billions of Discord-like messages (~50 lines) in a big storage system.
These notes will equip you with practical data analysis skills, the foundations for a problem-solving mindset for data systems, and help you tackle future data challenges. Get ready to take apart popular consumer applications, and have fun along the way!


Case Studies

Introduction

Section 1: Intro to SQL and Data Modeling

Case Study 1: Why does UberEats use SQL for faster product launches?
Case Study 2: How to build a basic Spotify with SQL?
Case Study 2.1: What about LLMs that produce “text to SQL”?
Case Study 2.2: How does SQL compare with alternatives like python and pandas?
Case Study 3: Why does Spotify store songs and lyrics in a key-value database?
Case Study 4: How do Spotify-like data apps work on your smartphone?
Case Study 5: How did Google handle data privacy and ethics for their COVID mobility reports?

Section 2: Storage and Indexing
Case Study 6: NanoDB – A small toy database
Case Study 6.1: How data apps store tables in IO devices?
Case Study 6.2: How NanoDB stores rows into DbFiles?
Case Study 7.1: NanoDB’s Algorithms for Hashing and Sorting
Case Study 7.2: How NanoDB models IO costs?
Case Study 8: How NanoDb indexes data to speed up searches?
Case Study 8.1: How do UberEats and Google Maps speedup geo queries using hashing in RAM?
Case Study 8.2: How do OpenAI’s apps and Facebook’s AI speedup queries using vector databases?
Case Study 8.3: How Spotify supports search on text?
Case Study 9.1: How BigQuery scaled to trillions of rows at Google?
Case Study 9.2: How to track user’s Spotify activity with high speed LSM trees in systems like BigTable and Cassandra?

Section 3: Query Optimization

Case Study 10: How could Spotify optimize basic queries?
Case Study 10.1: How NanoDB optimizes JOINs?
Case Study 10.2: Query Optimization in Spanner and SparkSQL
Case Study 10.3: Evolving Spotify’s data systems




Section 4: Transactions

Case Study 11: Taylor Swift and the Ticketmaster disaster
Concepts 11.1: How to build NanoDB’s transactions?
Concepts 11.2: Correct reorderings for concurrent transactions
Concepts 11.3: Locking protocols for interleaved micro schedules
Case Study 11.4: Taylor Swift on TicketsDisaster versus TicketsFaster?
Case Study 11.5: Logging for recovery
Case Study 11.6: How does NanoDB build transactions? [Optional Code]
Case Study 12.1: How to track user’s Spotify activity with high speed LSM trees in systems like BigTable and Cassandra?
Case Study 12.2: How does Google Docs work for collaboration?

Section 5: Distributed Systems

Concepts in Section: Why Distributed Systems?
Case study 13: Distributed Database Systems: Decouple Ticket Purchases,  Scalper Detection and Attack Mitigation
Case Study 14: How Google Ads builds on OLTP and OLAP queries?
Case Study 15: How Discord stores trillions of messages?

1. SQL and Data Modeling


Concepts: Schema, SQL operations, Primary and Foreign keys, Data privacy and ethics
Learning Goals
How to model a data app? How do we incrementally add new features to the app? (Case Studies 1, 2, and 4 on Spotify and UberEats) 
How to read and write SQL code? (Case Study 2 on Spotify recommendations)
When to use key-value DBs? (Case Study 3 on Spotify audio and lyrics storage) 
How to handle data privacy? (Case Study 5 on Google’s COVID mobility reports) 
Colab Spotify’s SQL examples
Exercise 1

Case Study 1
Why does UberEats use SQL for faster product launches?

Goal: Learn why modern data apps use SQL

Food delivery apps like UberEats and DoorDash are betting on the rapidly expanding and highly competitive food delivery industry. To gain market-share, UberEats experiments with different app features to quickly find what improves buyer and driver engagement, and drive new revenue streams. UberEats’ app teams use SQL, a popular programming language for data, to achieve product build goals, as follows. 
App features: For example, if UberEats wants to launch a new feature such as "frequent orders" for a buyer, the app teams can use SQL to quickly retrieve the data on the buyer’s previous orders and show them as a suggestion for their next order. Alternately, when launching a new feature such as "group ordering" for party orders, UberEats can use SQL to quickly retrieve the data on the buyers who have ordered together in the past and show them as a suggestion to other buyers.  
Real-time updates: The app team uses SQL to update the location and status of food deliveries. The app displays this information to the buyer in real-time, allowing them to track the progress of their food delivery. Restaurants can update their food capacity (e.g., no more salads for the meal) through a restaurant portal (also powered by SQL). Furthermore, SQL is used to monitor and act on a delivery partner's performance.
Data analysis and optimization: UberEats uses SQL to analyze data on how users interact with the app, such as which features are most popular or which areas have the highest demand for food delivery. This information is used to optimize and improve the user experience. For example, SQL can be used to identify the most popular dishes in certain areas, and increase the inventory of those dishes in those areas.
But wait a minute…I read a blog saying SQL was slow, and only ancient companies use it. Did I read that wrong? 
Welcome to your first lesson! Over the past 20 years, sub-fields in Computer Science (CS) have experienced significant cycles of growth and decline, similar to a pendulum swinging back and forth. These cycles have included ``AI winters,’’ ``noSQL movements,’’ ``chip design winters,’’ among others. Often the predominant use cases change, and the sub-fields are reinvented around a few core principles. 
In the 2020s, SQL is experiencing a big upswing for “modern” data stacks, and we expect this trend to continue for several years. To gain a better understanding of past and future cycles, it’s crucial to understand why these changes occur, and the fundamental principles that underpin each field. In the rest of this chapter, we highlight the core of these changes.  
In the early 2000s, SQL databases, which were the most popular databases at the time, were designed to work on a small number of high-end, expensive and ultra-reliable servers to process data tables in banks, retail and e-commerce. However, they became ineffective and costly to manage the rapidly growing web-scale data, such as web pages, user activity, and media. At the same time, big players like Google and Amazon changed the game by building (cloud) data centers with millions of cheap, commodity servers. App engineers started to build appropriate data stacks and new hybrids for the specific use cases they were tackling. For example, Google picked a hybrid approach based on the use case.
Google's web search and Gmail stacks, for example, could not be built with SQL or traditional databases in the market, because they were not equipped to handle these new use cases and scale in a cost-efficient way. As a result, Google engineers adopted, adapted, and invented a variety of techniques to build large-scale distributed systems to support these new use cases. These included Google File System (GFS), MapReduce for processing data, and BigTable for key-value stores. In parallel, industry dubbed this as the start of the noSQL movement, and built Hadoop and various commercial products. 
Google's critical Ads stack, which powered Google’s billions in revenue, was built around MySQL and custom servers interfacing with MySQL. These apps needed the reliability and flexibility of SQL systems to help app teams to rapidly iterate on customer needs. 
In the past 10 years, the data community has revamped database engines to adapt to cloud clusters, new data types, new API languages, and new use cases, while keeping SQL as a common language. For example, in the past few years, Google’s ~100 billion$/year ads system replaced MySQL with a new globally-distributed and SQL-based scalable database. The broader industry has also quickly adopted these next-generation engines for a few key reasons: 
SQL is a lingua franca for an estimated 20 million + (and growing) app developers in 2023.  SQL's widespread use has also led to a large community of developers who are familiar with the language and can help each other troubleshoot and optimize their code. This community has created a wealth of resources, from online tutorials and forums to code libraries and open-source projects, making it easier for developers to get started with SQL and continue to improve their skills over time. 
As a declarative programming model, focused on expressing what needs to be done rather than how to do it. It’s akin to the convenience of the new tools in generative AI, where you express what you want rather than specifying how it’s made. 
For a powerful ecosystem of tools. When databases are connected to one another, and as the connections between databases grow stronger, the potential for valuable insights increases. This is similar to Metcalfe's law of quadratic value, which states that the value of a network grows exponentially with the number of connected users. Many data-oriented products switched to SQL as a ‘standard’ data-centric interface, rather than maintaining additional API layers for data exchange.
At the same time, key-value stores have gained in popularity for specific use cases (e.g., semi-structured data and media). We’ll see an example Case Study 4 on Spotify’s audio and lyrics database. 
Here is an excellent summary of why and how Google’s Spanner evolved from a pure key-value store to a SQL system. Keep your focus on the big picture and get a flavor for tradeoffs. (It’s a PhD level paper, so I don’t expect you to understand all the details.)


Case Study 2
How to build a basic Spotify with SQL?

Goal: Learn how to read and write SQL through practical examples. See tradeoffs with Python and Pandas for big data. 

Music lovers use Spotify to discover and listen to music, podcasts, and other audio content. Users can create and share playlists, follow their favorite artists and podcasts, and discover new music based on their listening preferences. Spotify offers both a free, ad-supported version and a paid, ad-free version of its service. Spotify also provides additional features for artists and creators. Creators can upload and promote their content, and access detailed statistics and insights about their listeners. That is, Spotify needs to have a flexible database to support the above use cases, and to build new experiences for users, creators, and advertisers.
In this case study, we create a basic version of Spotify.
First, we set up 3 tables, and write our first SQL query to identify popular songs. 
We then implement a new feature request to provider users with playlist recommendations. We add a fourth table and write our next SQL query.
Finally, we write some (intermediate) SQL to compute recommendations (for Step 2) using collaborative filtering (suggest songs that are commonly shared among users who only listen to one of the songs.).
We use a companion notebook, Spotify's SQL examples Colab, with a live SQlite database. For each of our Examples, play with the corresponding section in the Colab.


Definitions
Schema: A blueprint that defines the structure and organization of a database. Includes details such as table names, columns, data types, and relationships between tables.

Motivation: Schemas enable clear and consistent organization of data in a database, making it easier to manage, query, and optimize data. They also improve developer productivity by providing a clear understanding of the database structure, making code more readable and maintainable. Furthermore, schemas enable the evolution of data over time by allowing for changes in the database structure as requirements change.

Table: A collection of organized data in a database, consisting of rows and columns. Each column represents a specific attribute or field, while each row represents a single record or instance.

Motivation: Tables provide a structured way to store and process data, making it easier to search, modify, and analyze information. They also resemble spreadsheets, offering a familiar and intuitive way for engineers to represent and interact with data, allowing for quick insights and data analysis.
Primary Key: A unique identifier for each record in a table. It ensures that no two rows have the same value, enabling fast searches and updates of rows.

Motivation: The primary key's uniqueness helps maintain a clear and organized structure within the database. It allows for precise identification and retrieval of individual rows and prevents duplicate entries, which can lead to data inconsistencies and confusion. By enforcing unique values, primary keys help keep databases accurate, reliable, and easily searchable.
Secondary key: A non-unique attribute or set of attributes in a database table that enables efficient access to rows based on values other than the primary key.

Motivation: Applications can use such keys for alternative search, sort, and filter options. particularly in large or complex databases. For example, artist name could be a (non-unique) secondary key, while artist ID would be a primary (and unique) key.
Foreign Key: A column or set of columns in one table that refers to the primary key in another table. It is used to establish a relationship between two tables.

Motivation: Foreign keys provide a means to connect and synchronize data across different tables. By referencing unique primary keys from another table, foreign keys ensure that related data is consistent, accurate and we avoid orphaned records. 


Example1: Basic version of Spotify (Intro SQL)


This SQL schema defines three tables to support a basic version of Spotify’s features: 
The Users table contains information about each user, including their name, email address. The user ID is a primary key, a unique integer we use to refer to a user. We use the VARCHAR type for small strings and TEXT for big strings.
The Songs table contains information about each song, including the song ID (a primary key), title, and artist and genre (secondary keys to support artist and song search).
The Listens table contains a record of each time a user listens to a song, including the listen ID, the user ID, the song ID, and the time the song was listened to. We also see foreign keys to the Users table. That is, every user_id in Listens has to refer to a user_id in the Users table. Similarly, every song_id in Listens refers to a song_id in the Songs table.

We see example rows in the tables. For example in the Users table, Mickey has user ID =1 and mickey@example.com as his email. Similarly, we see the rows in the Songs and Listens tables. 

Also, notice we have no data for any of the Listens.listen_time values, and these values are set to None. It’s common for tables to have some missing data, and these are marked as NULL or None. We mark the required and optional fields in the schema. For example, Listens’ listen_time and ratings are set up as optional columns (and could be NULL).  The other fields are required – listen_id (because it is a primary key), user_id (NOT NULL), and song_id (NOT NULL) are required. 




Popular songs: Let’s compute the top 10 songs users listen to. For example, see the expected output table. We annotate parts of the query to highlight the output, input, and logic.

In this query, the DB 
Outputs 3 output columns: (1) song title, (2) artist, and (3) popularity count  (the number of listens for each song).
Takes two input tables – Songs and Listens tables, and joins (matches) them on the song_id column. 
Then it groups the results by the artist and title columns, so that we can count how many times each song has been listened to. 
Next use the COUNT() function to count how many times each song has been listened to. Then order the results by the number of listens in descending order, so that the most popular songs are at the top. 
Finally, limit the results to the top 10 most popular songs. 

Here’s the equivalent python code for the popular songs SQL query. 

The provided Python code shows a procedural approach where we iterate over dictionaries in memory to compute the desired values using for loops. On the other hand, SQL is a declarative language where we specify what we want, and the database engine decides the most efficient way to execute the code.
Also, the Python code assumes that the songs and listens data are stored in dictionaries in RAM of a single machine. In contrast, SQL works with tables without making assumptions about their storage location, size, or distribution. The tables could span billions of rows, on a cluster of machines, and the database system optimizes the execution plan to efficiently retrieve the desired results regardless of the scale and distribution of the data.


Concepts: SQL operators
SELECT operator: This specifies the output columns needed after running the query. In the Popular Songs query, we select these columns - title, artist and COUNT(listens.song_id) renamed AS popular, from the Songs and Listens table.
FROM operator: This specifies the input table(s) from which the data is retrieved. In this query, we are retrieving data from the Songs and Listens tables.
JOIN operator: This operator specifies additional input tables to combine rows from two or more tables based on a related column between them. In this query, we are joining Songs with Listens on the song_id column.
WHERE operator: This operator is used to filter the rows of a query based on a specific condition. It is used to narrow down the results of the query by specifying certain criteria that must be met for a row to be included in the final output. The rows for which the condition is true are included in the final output, while the rows for which the condition is false are excluded. We’ll see an example in the next query. 
GROUP BY operator: This operator is used to group the results by one or more columns. In this query, we are grouping the results by the artist, song columns, so we can count how many times each song has been listened to.
COUNT() function: This function is used to count the number of rows in a column. In this query, we are counting the number of times each song has been listened to by counting the number of rows in the listens.song_id column that have the same song_id value.
ORDER BY operator: This operator is used to sort the results by one or more columns in ascending or descending order. In this query, we are ordering the results by the listens_count in descending order, so that the most popular songs are at the top.
LIMIT operator: This operator is used to limit the number of returned rows from the query. In this query, we are limiting the results to the top 10 most popular songs.
Example2: Computing Average Ratings (Intro SQL)

Average ratings:  Let’s compute average ratings for all songs, including songs with no ratings. For example, see the expected results table. (Equivalent python code)

In this query, Songs is joined with Listens using the song_id column. The join is a LEFT JOIN, meaning that 
All records from the left (Songs) table will be included in the result, and any matching records from the right (Listens) table will be included. 
In addition, if a song in the Songs does not have a corresponding rating in Listens, then the result will include a NULL value for the rating column. 
LEFT JOINs are an extension of JOINs. We include tuples from the left table that do not have matching values in the right table. 

Similarly, RIGHT JOINs will include tuples from the right table that do not have matching values in the left table. Finally, FULL JOINs (also called OUTER JOINs or FULL OUTER JOINs) will include missing tuples from the left and right tables, and fill in missing columns with NULL. 

Example3: Adding Recommendations table to Spotify (Intro SQL)

Recommendations: To support song recommendations (a “new feature” request), we add a new table to the above basic schema. The Recommendations table stores song recommendations for a user, which includes recommendation_id, user_id, song_id, and recommended_time.

Also, we can add an index on the user_id column in the Listens table to speed up searches for songs listened by a specific user. We could also index Recommendations table on multiple columns (e.g.. <user_id, song_id> pair)  for fast multi-columns lookups. In general, we can create multiple indices, on one or more columns in one table. 

Per-user song Recommendations: Let’s say, Minnie wants song recommendations. See the expected results in the results table. (We’ll see how to compute Recommendations in the next Section.) 

In this query, we first join Songs with Recommendations on the song_id column. Then we filter the results with Minnie’s user ID, using a subquery (a “nested query”).

Concept
SUB-QUERY: We use these to retrieve data from the table based on the result of another query. In Minnie’s song recommendations query (Example 3), we are retrieving the user_id from the users table where the name is 'Minnie' and using it in the main query to filter the results.
Tip: How to read SQL?
Reading SQL for SPJ (Select-Project-Join) queries can be overwhelming at first, but it becomes easier with practice. Here are some general tips on how to read such queries:
What’s the goal of the query? Start by understanding the goal. For example, the goal of the song recommendations query is to find the title and artist of the recommended songs for the user 'Minnie'.
What’s the input and output? 
The SELECT clause is the output of the query. In this case, the output of the query consists of the title and artist columns from the Songs table. Rest of the query is about computing this output. 
Scan the query and find the input tables involved in the FROM and JOIN clauses.
What’s the logic to reshape data from the input tables? Read the rest of the query (from top to bottom), starting with the FROM or JOIN clause (the input tables), then the WHERE clause, ORDER BY and finally the LIMIT clause. Each clause plays a specific role in the query and helps to filter and shape the data for the next step. Understand how each clause reshapes the data to the next step.
For any subqueries (e.g., SELECT user_id from Users where name = ‘Minnie’), apply the same steps to work out the goal of that specific subquery and what its output will feed into the full query (similar to how functions call other functions).  
Example4: Computing Recommendations table (Intermediate SQL)


Now let’s compute a per-user Recommendations table based on collaborative filtering. That is, each user gets a list of song recommendations based on what other users also listen to. (Equivalent python code) 

This query uses Common Table Expressions. CTEs are similar to python/java functions and help us write modular SQL.
The song_similarity CTE computes the number of common users who have listened to a pair of songs. It joins the Listens table twice, once as u1 and once as u2. The join condition is that the users are the same and the song IDs are different. The results are then grouped by the song IDs and the HAVING clause is used to filter out pairs of songs that have fewer than 10000 common users. We see the results in the Song Similarity table. (In this example, we’re listing common_users > 1, rather than 10000.) For example, in the 5th row we see that two users listened to both song_id= 6 and song_id=1. 
The recs CTE joins Listens with song_similarity on the song ids to find similar songs. The CTE then inserts a new song for a user only if it does not already exist in the user's Listens. This is achieved by using a subquery to select the song_id from the Listens table, where the user_id is equal to the user_id from the main query. For example, in the Recs table, we see two new recommendations for user_id=2.
Finally, we insert the results into Recommendations so we can use it for subsequent queries without recomputing the CTEs.  






Example5: Computing Average ratings of songs (Intermediate SQL)




Next, let’s discuss different queries  related to song ratings. (Equivalent python code)
The first query uses GROUP BY to group the rows by user_id and song_id, and then performs the sum and average calculations on each group.
The song_ratings CTE selects the user_id, song_id, and rating columns. It also calculates the total ratings per user using the SUM(), with the OVER clause on the PARTITION (subset) of the table defined by the user_id. This means that the SUM() function will sum the total ratings for each distinct user_id in the table. The OVER+PARTITION operators are also called window functions.
In the third query, we calculate the ratio of rating to the ratings_sum. That is, the ratio of each song rating to the total ratings of the user. (Intuition: contribution of a user’s rating to overall rating). 

These queries feel ‘similar’ but give us different results. We show the results of the two queries. Specifically, the song_ratings CTE sums the overall ratings per user, and uses that for the per-song ratings. By contrast, the GROUP BY groups user_id and song_id, and will have the same values for avg_rating and sum_rating because it groups by user_id and song_id.

So, based on your use case, you can use either window functions or GROUP BY to perform calculations on a set of rows, but they have different semantics, and will give you different results. 


Intermediate Concepts: More SQL operators
SUB-QUERY: We use these to retrieve data from the table based on the result of another query. In Minnie’s song recommendations query (Example 3), we are retrieving the user_id from the users table where the name is 'Mickey' and using it in the main query to filter the results.
Common Table Expressions (CTEs) allow a query to reference a temporary result set defined within the query itself. They are used to simplify complex queries by breaking them up into smaller, more manageable pieces. CTEs are defined using the WITH clause, followed by a SELECT (or INSERT) statement and a name for the CTE. For example, see song_similarity: This CTE calculates the similarity between each pair of songs by counting the number of common users who listened to both songs. 
WINDOW (PARTITION BY and OVER). A window function is a type of SQL function that performs a calculation on a subset of rows in a table, rather than all the rows. In our example, OVER() picks rows that have the same user_id, and uses the SUM() function to calculate the total ratings per user. The subset of rows is defined by a window, which is specified using the OVER() clause. A window function can be used for a variety of calculations, such as calculating running totals, averages, or ranking of rows. These calculations are done on the current row and a set of rows that are defined by the window. One of the main advantages of window functions is that they allow for more efficient querying, as they can perform calculations on a subset of rows, rather than all the rows in the table. This can be more efficient than using multiple self-joins or subqueries. For example, a query that calculates the running total of a column for each row in a table can be done with a window function, instead of a self-join. It can also be used to calculate the average rating of a song from all the ratings, the ranking of a song based on the ratings, or the difference of a rating from the average rating per song.

Case Study 2.1
What about LLMs that produce “text to SQL”? 

Goal: Learn about correctness of SQL code, equivalent queries


We can use large language models (LLMs) to help convert text to SQL by analyzing natural language input to identify key entities, relationships, and operations, then structuring these into SQL syntax. GPT, Claude and Gemini’s LLMs are now good training ``copilots’’ for learning SQL. Also, it is convenient to convert natural language into instant translations making it easier for non-experts to query available data. At the same time, it’s important to note that the queries might be correct in syntax but flawed in logic or may misinterpret the requirements, leading to incorrect results. Also, it’s important to carefully analyze edge cases and specific conditions to look for semantic errors.
In 2023, Google’s DeepMind reported 77% accuracy for ``text to SQL’’ on one benchmark. https://ar5iv.labs.arxiv.org/html/2306.00739. We can expect the quality of LLM-generated SQL queries will continue to improve as models become more sophisticated and are trained on larger, more diverse datasets. Advances in prompt engineering, fine-tuning, and error correction will also enhance their accuracy and reliability​. However, until we get Artificial General Intelligence (AGI), which would possess human-like understanding and reasoning capabilities, we need to continue to be careful about logic problems. For many financial applications and healthcare applications, 80-90% accuracy in logic will be unacceptable. Of course, incorrect logic is not a LLM-specific problem but often happens even for senior engineers and analysts. 
Let’s consider how to analyze if a query produces the required output, or if two or more queries are semantically equivalent, independent of whether Claude or OpenAI or an engineer writes SQL code given some text prompts or requirements. 


Query Equivalence
Understanding query equivalence is key for correctness and reliability of SQL queries generated by both humans and LLMs. There are two primary types:
Output Equivalence:
Definition: Two queries are output equivalent if they produce the same output for a specific given input.
Testing: This involves running both queries on the same dataset and comparing the results.
Use Case: Useful for specific scenarios where the context is well-defined, and variations are minimal.
Logical Equivalence:
Definition: Two queries are logically equivalent if they produce the same output for any given input.
Testing: This requires a thorough analysis of the query logic to ensure they handle all possible inputs in the same way.
Use Case: Crucial for broader applications where the query needs to be robust against various data sets and conditions.

In the following discussion, we'll examine two sets of SQL queries that appear similar but have subtle differences. We'll use these examples to demonstrate effective techniques for query analysis and debugging. First, we'll break down each query into its component parts, write out debug tables, and trace through the results at every stage of execution. This step-by-step approach is crucial for understanding query behavior and identifying potential issues. 
Example1 for testing Logical Equivalence  


Example2 for testing Logical Equivalence  




Tips for identifying logic errors
When working with SQL, especially SQL generated by LLMs, pay particular attention to:
NULL handling: Always consider how NULLs are treated in your queries. Use IS NULL/IS NOT NULL for comparisons.
DISTINCT usage: Be cautious with DISTINCT. It can hide data quality issues and may not always be necessary, especially when used with aggregations.
JOIN types: Understand the differences between INNER, LEFT, RIGHT, and FULL OUTER JOINs. Be especially careful with LEFT JOINs in combination with WHERE clauses, as they can sometimes behave like INNER JOINs.
Aggregation logic: Always ensure your GROUP BY clause includes all non-aggregated columns in the SELECT list.
Subqueries and CTEs: For complex logic, consider using subqueries or Common Table Expressions (CTEs) to break down the problem into smaller, more manageable parts.
Edge cases: Always consider edge cases in your data, such as users with no activity or items with no ratings. Always test your queries with diverse sample data, to verify that they produce the expected results.
By keeping these points in mind, you can more effectively leverage LLMs for SQL generation while avoiding potential pitfalls and semantic errors.


Case Study 2.2
How does SQL compare with alternatives like python and pandas? 

Goal: Learn about python+pandas alternatives to SQL

While SQL remains a popular data processing language, let’s review some alternatives to get a flavor for the tradeoffs.
Procedural languages: Python, C++, and Java offer distinct approaches to big data processing. Python's simplicity makes it ideal for interactive data manipulation. C++ excels in performance-critical scenarios with its speed and low-level control, at the cost of development complexity. Java's portability and strong ecosystem provide scalability and parallelism advantages. Each language's trade-offs—Python's interpreted nature and memory consumption, C++'s complexity, and Java's performance overhead— should be considered while building a custom application.
Python plus libraries like Pandas: Pandas, with python, offers a versatile approach to data manipulation and analysis. Its intuitive DataFrame structure simplifies handling structured data, while versatile functions handle diverse types and missing values. It supports over 600 functions optimized for efficient analysis, indexing, and aggregation. Pandas' compatibility with various formats and memory efficiency make it invaluable for data tasks.
Custom variants and derivatives of SQL: Apache Spark is a popular, open-source distributed computing system for big data processing and analytics. Spark supports SparkSQL to support SQL operations on Spark data, in addition to other custom APIs. Similarly, CQL (Cassandra Query Language) works on Cassandra, another popular open-source data system. 


We represent our example tables – Songs, Listens and Users as python arrays in this example. The "songs" dataset includes song details like ID, title, artist, and genre. The "listens" dataset records user interactions with songs, including listen ID, user ID, song ID, and a rating. The "users" dataset holds user information such as user ID, name, and email address. 

This example Python code computes the most popular songs, similar to the SQL code we saw earlier. The function calculates the listen count for each song by iterating through the listens. It then creates a list of popular songs with their titles, artists, and listen counts. The list is sorted in descending order based on the listen count. Finally, the top 10 popular songs are displayed. 


The code snippet uses the Pandas library to calculate popular songs. It begins by converting the "songs" and "listens" datasets into Pandas DataFrames. Then, the code employs a series of Pandas functions to process the data. It merges the two DataFrames based on the song ID, groups the data by song title and artist, counts the number of listens for each song, sorts the results in descending order of listen count, and selects the top 10 popular songs. Finally, the code prints the top popular songs.
This Pandas code shares a similar objective with the SQL code we saw earlier. However, while the SQL code used SQL queries and operations, this Pandas code uses DataFrame operations to achieve the same outcome. Both approaches involve data manipulation and aggregation to identify the most popular songs, with the key distinction being the choice of programming language and library.



When to use Pandas versus SQL based solutions?
Pandas' Strengths and Weaknesses: Think about working with a Spotify dataset containing 10,000 Songs and 10,000 rows in Listens using Pandas. All this data will fit in RAM on a single machine. With 600+ functions, data scientists often find Pandas convenient to load data into RAM on a single machine, and to analyze and visualize this dataset. However, when handling Spotify's entire library of millions of songs and user data, Pandas will struggle due to memory limitations. 
Scaling and Exploring Alternatives: Consider wanting to analyze the complete Spotify library of 50 million songs and 100s of millions of rows of user’s Listens data. In such a case, relying solely on Pandas might not be practical. This is where SQL-based frameworks are designed to process immense datasets by splitting tasks across multiple machines, and making it seamless for the data app developer. 
Future potential solutions: A few research projects and startups are trying to bridge the above gap. For example, Modin from Berkeley’s database group rewrites the 600+ pandas calls into SQL, so the app developer can use pandas, while the backend executes on a SQL-based backend. In 2023, they report scaling up to a Terabyte of data, and speeding up Pandas by 16x for some workloads on BigQuery.  
Case Study 3
Why does Spotify store songs and lyrics in a key-value database?

Goal: Learn when to use key-value databases


Definitions

Structured data (or Tabular data) refers to tables of organized, formatted data that is easily stored and managed in fixed fields, such as rows and columns in a spreadsheet or a relational database.

Motivation: Structured data enables efficient storage and manipulation, making it suitable for applications like Spotify's tables of integers, strings, and simple types, we saw in Case Study 2. SQL also supports arrays and vector types. 
Unstructured data includes complex types such as media files, textual content, or user-generated data from social media platforms.

Motivation: Allows databases to support complex types for richer information and insights. For example, Spotify could store audio files for songs, and leverage unstructured data from social media to enhance its recommendation systems.
Semi-structured data lies between structured and unstructured data. It is not strictly organized into fixed fields like structured data, but it still has some level of organization, often following a loose format or schema. 

Motivation: JSON (JavaScript Object Notation) blobs are a common example of semi-structured data, where data and types are flexible, and elements can be nested or follow varying structures. Semi-structured data, such as JSON blobs, offers a balance between the rigid organization of structured data and the flexibility of unstructured data. The loosely defined schema in semi-structured data enables easier integration and transformation, facilitating the handling of complex or changing data requirements.

For unstructured and semi-structured data, Spotify can use a key-value database, such as Google’s Bigtable or AWS’ DynamoDB, to store audio files in order to improve the performance of retrieval of audio content to its users. For example, Spotify can use the song's unique ID as the key and the audio file as the value in the key-value database. When a user requests to play a song, Spotify can use the song's ID to quickly retrieve the audio file from the key-value database and stream it to the user. Spotify could also use a distributed file system (e.g., Amazon's S3)) to store audio files, and use the key-value database as an index to store the file location and retrieve the audio files. This approach allows Spotify to scale to store and serve a large number of audio files and also improve the performance of streaming of audio content to its users.
Could we store unstructured data in a regular SQL database?
Yes, we could. SQL databases support blob types, where we store any binary object. However, here are some important trade-offs to consider. Also, in some `hybrid’ products SQL databases support key-value data as a feature. Here we focus on the ‘conventional’ definitions  
SQL databases provide rich query capability, where you can perform complex queries, joins, and aggregations. They need a predefined schema to store data. SQL databases are known for their strong data integrity, as they enforce data constraints, transactions, and referential integrity through the use of primary keys, foreign keys, and other constraints. All these create some overhead.
Key-value stores are much simpler databases, and often better suited for large unstructured and semi-structured data. Given a key, it returns a value. They do not require a predefined schema and are more flexible in terms of data modeling. For example, we’d store the lyrics for a song with {key=songid, value = lyrics}. We would not want to store each line in the lyric (say) in a separate column. Also, we may store the media file on a distributed file system (such as Amazon’s S3), and maintain a key-value database for {key=songid, value= S3-location}, rather than storing the media in a structured database. 

Case Study 4
How do Spotify-like data apps work on your smartphone?

Goal: Learn how to build data apps on smartphones (and portable devices)

Spotify users can listen to their music by accessing the data in the cloud service, or on-the-go in offline mode, by downloading playlists and music when they have a stable internet connection and listening to it later (e.g., on airplanes). When in offline mode, Spotify users have access to a limited set of features compared to when they are online. Some examples of what a user could do when in offline mode include:
Listen to their saved content, including albums, playlists, and individual tracks. Users can play and skip songs in their saved playlists, albums and tracks
Explore and make modifications to their playlists by adding or removing favorite songs. When the user is back online, these changes will be synced to the user's preferences on the cloud, ensuring a seamless transition across devices.
From a technical standpoint, the app needs to address a few key issues for the user on their device: managing the necessary user data and synchronizing any changes with the cloud once a connection is established.
The good news is that Android, iOS, and popular web frameworks (e.g., react) support SQLite in their developer SDKs (i.e., preinstalled on 3 billion + phones). SQLite is a popular, self-contained, fast, serverless, and transactional SQL database engine. It requires minimal setup and administration, making it easy to integrate into mobile apps on devices with limited resources. Also, SQLite is open-source software, and can be freely used, modified, and distributed. SQLite is widely supported and has a large community of developers and users. 
With SQLite, developers can easily create, read, update and delete data in their apps without the need of any additional custom code or setup and hence it becomes a convenient and efficient way of storing and synchronizing structured data for mobile apps and the cloud.
Here’s one such example of how to build Spotify’s offline mode on a user’s device using SQLite. 

Here’s an example SQL schema on the device. It’s quite similar to the SQL schema we may use in the cloud. We’ll focus on the unique parts in this schema.
Songs table’s file_location stores the location of the audio file on the device.
Playlists table’s created_at and updated_at columns store the timestamp of when the playlist was created and last updated respectively.
Playlist_tracks table’s added_at stores the timestamp of when the song was added to the playlist. Also, notice that the primary key is a compound key, based on both playlist_id and song_id.



This query uses two CTEs to select only the Playlists and Playlist_tracks that have been updated within the last 600 seconds. The datetime('now', '-600 seconds') is a SQLite specific way of getting the current timestamp minus 600 seconds.

You can use these CTEs as a starting point to build the rest of your query that will synchronize recent changes with the cloud, once every 600 seconds. In fact, many apps use such synchronization techniques periodically when a device is on a cellular connection both for speed and to save costs.



Case Study 5
How did Google handle data privacy and ethics for their COVID mobility reports? 

Goal: Learn the basics of data privacy and ethics, both rapidly evolving fields

(This section does not endorse Google’s specific approach, but aims to provide insight into a few areas of concern when data and policy issues converge.) 
During the COVID-19 pandemic, several tech companies, including Google and Apple, published anonymized mobility reports to provide insights into changes in human movement patterns from smartphone data. These reports were designed to help public health authorities and policymakers in making informed decisions to slow the spread of the virus. 
Such mobility reports contain information about visits to sensitive locations, such as hospitals or COVID-19 testing centers, with the number of visits and timestamps. While the data is anonymized, it still poses a risk of re-identification attacks. We share a screenshot from Google’s privacy stance to highlight 3 concepts (1) what user consent Google used to collect user data, (2) links to how Google secures user data, and  (3) how the data was aggregated and anonymized. 

Re-identification Attacks
Consider an attacker who wants to find out if their colleague Bob visited a COVID-19 testing center on a specific day. The attacker knows that Bob was feeling unwell and took a day off from work. The attacker examines the published mobility data and finds only one visit to a testing center near Bob's home on the same day he took the day off.
Since the visit and timing are unique in the dataset, the attacker can confidently deduce that Bob went to the COVID-19 testing center. This reveals sensitive information about Bob's health and potentially his COVID-19 status, which is a violation of his privacy. Similarly, we need to be careful when aggregating and anonymizing users' activity data, especially for sensitive locations such as religious institutions and healthcare facilities, or when dealing with users' watch history, which reveal the types of content they consume.
Privacy-preserving techniques
K-anonymization is a simple heuristic for protecting privacy in which individuals in a dataset are grouped together based on shared attributes (e.g. demographic clusters of size >=k) to make it more difficult to identify specific individuals. However, such heuristics are vulnerable to re-identification attacks and often produce data with low utility.
Differential privacy provides a more solid framework with mathematically proven strong privacy guarantees, even when attackers have access to additional information about the dataset or the individuals within it. This is why differential privacy has become the preferred technique for privacy protection in data analysis. By adding ``mathematical noise’’ using differential privacy to the COVID mobility reports, Google can release useful aggregates and APIs for crises, while protecting users from re-identification attacks. 
``Zero knowledge’’ training is another technique that allows machine learning models to be trained on encrypted data without revealing the underlying data to the model or to the trainer. For example, you can partition data across workers, and each worker only has access to a subset of the encrypted data, and performs computations on that subset without knowing the values of the other data points. By aggregating the results of the computations performed on each worker's subset of the data, the model can be trained on the entire dataset without revealing the underlying values. While differential privacy is focused on protecting the privacy of the data itself, zero knowledge training is focused on training machine learning models without revealing sensitive data. 


In SQL Colab, we have a brief example to generate COVID mobility reports using SQL. The following SQL query operates on a user_location_activity table to produce the following results.

The query retrieves the count of visits per location for a specific date range, grouped by location_id and location_type.



To protect individual privacy, we can use Google's PYDP library to apply differential privacy to the visit counts obtained from the SQL query. The PYDP library adds "noise" to the results, preserving the overall trends while making it difficult for attackers to re-identify specific individuals. Here's an example of how to use the PYDP library to adjust the counters with noise.

Notice that each time you run this code, you'll get slightly different results due to the random noise introduced by the differential privacy algorithm. However, the overall trends in the data will still be preserved.

Concepts
Data privacy and ethics is an important, broad, and growing topic. In this brief overview, we will summarize a few key topics to keep in mind while building consumer data applications, to raise awareness of the potential challenges and provide guidance on responsible data practices. (Optional: Read System Error and Ethics and Data Science.)
Privacy and Anonymity: Protect your users' privacy and personal information. This means using techniques like data anonymization to make sure individuals can't be identified. You can also implement differential privacy when sharing aggregate statistics or insights.
Informed Consent: Make sure that your application's terms and conditions, privacy policy, and any consent forms are easy to understand and clearly explain how users' data will be collected, stored, and used. It's important to provide users with the option to opt-in or opt-out of data collection and consider implementing granular consent settings for different types of data processing.
Data Collection and Bias: Be aware of potential biases that can be introduced during data collection and make sure that your data is diverse and representative to minimize the risk of bias. When building data-driven applications, strive to make them transparent and explainable to users. You should also actively monitor and evaluate your algorithms or models across different user demographics. This will enhance user trust and help identify any ethical issues that might arise from the use of data.
Data Security and Breaches: Ensure that your consumer application implements robust data security measures to protect sensitive information from unauthorized access or breaches. When sharing data with third parties, make sure it's done responsibly with good de-identification techniques.
Legal and Regulatory Compliance: Adhere to all relevant data protection laws and regulations. For example, the General Data Protection Regulation (GDPR) requires that personal data of European Union citizens be stored and processed only within the EU or in countries with an adequate level of data protection. Similarly, the California Consumer Privacy Act (CCPA) requires that organizations provide consumers with the ability to request that their personal data be deleted.  Health Insurance Portability and Accountability Act (HIPAA) regulates how electronic protected health information (ePHI) is handled by healthcare providers and applications. Failure to comply with these laws and regulations result in legal and financial consequences. 

Takeaways
Gaining user trust in applications we build helps ensure that our work has a positive impact. 
Incorporate data ethics principles into the design and development of data applications. Remember, this is an ongoing process, and it's important to keep learning and reflecting on data ethics topics. 
Don't hesitate to seek guidance from experts and resources to help you navigate any complex challenges that may arise.


Summary of Section 1
Concepts: Schema, SQL operations, Primary and Foreign keys
Learning Goals
How does an app model data? How do we incrementally add new features to the app? (Case Studies 1, 2, and 4 on Spotify and UberEats) 
How to read and write SQL code? (Case Study 2 on Spotify recommendations)
When to use key-value DBs? (Case Study 3 on Spotify audio and lyrics storage) 
How to handle data policies and privacy? (Case Study 5 on COVID mobility reports) 
Exercises 
Play with examples in Spotify's SQL examples (Colab)
Practice with SQL projects (Links in course website) 
Optional? Do Kaggle data challenges. Read System Error and Ethics and data science

Takeaways and Tips
In real applications, it’s common to store structured data as tables in relational databases, while semi-structured data is stored in key-value databases. For simpler apps with a mix of both structured and semi-structured data, it's often best to choose one database that best fits the app's primary use case, as deploying and maintaining multiple databases can be excessive.
SQL is a popular language for parallel data processing in clouds and millions of CPU cores, to smartphones with a few CPU cores. ANSI SQL is a standard. However, in practice, databases often have custom extensions and variations in their language dialects. To effectively use any specific database, it's important to first learn the core SQL language (our goal for this Section), and then consult product-specific documentation. 
To read SPJ (Select-Project-Join) queries, read the query in sequence from top to bottom. Start with the SELECT clause, the output.  Next, examine the FROM/JOIN clauses, the input tables. Next, understand how the core logic from ON, WHERE, GROUP BY, ORDER BY, HAVING clauses reshape the data to produce the final output.
2. Storage and Searches



Concepts: Hash partitioning, Indexes (Basic, Sorted, B+ tree, Text, Locality Sensitive), Columnar vs Row-based storage

Colab: NanoDB – Simple toy database to learn about storage (~100 lines), indexing (~200 lines) and join algorithms (~300 lines). Hashing examples for text, and high dimensional data
Learning Goals
How to store data and model costs in RAM and disks? (Case Study 6)
How Spotify and UberEats search over complex data fast? How to build fast indices on complex data types and high-dimensional data? (Case Study 7, 7.1, 7.2) 	
When to use columnar stores versus row stores? (Case Study 8 on BigQuery)
Exercise #2

Case Study 6 
NanoDB – A small toy database 
Goal: See how to build a functional database through examples and code

We introduce NanoDB (in Colab), a small toy database to help build intuition for how databases store, index, and process data. NanoDB is implemented as a Python library and can be used within a Jupyter notebook or Google Colab. Through NanoDB, we will explore different techniques used by databases to store data and optimize performance. In the following sections, we will delve into the details of these techniques, showing how they are implemented. 

Definitions of key components in NanoDB
IO Devices are the physical devices where the data is stored, and where we read data from and write data to. For example, RAM, Hard Drives, Solid State Drives.  
Motivation: In a machine, RAM is ideal for small, frequently accessed data that requires fast input/output (IO or I/O) operations. SSDs (Solid state disks) are suitable for big data that is not frequently updated, while HDDs (Hard disk drives) are ideal for long-term storage of massive amounts of data. Systems designers pick different IO devices based on the specific needs of the data and the costs involved.
A logical table refers to the schema and the relationships between data elements and how they should be accessed and manipulated by the application. 

Motivation: In Spotify, data for Users, Songs, and Listens are organized logically into rows with columns representing specific information for each record. This organization is independent of how the data is physically stored, whether it's on a single smartphone or spread across thousands of machines, or how the underlying hardware evolves over time. 

A DbFile (or physical table) refers to the actual storage of data on an IO device, such as RAM, hard drives or solid-state drives. It includes information about how data is stored (e.g., file format, location, size) and provides functions for reading and writing pages from the file. 

Motivation: DbFiles are an extension of a regular file in the operating system. The database directly manages the low-level details of storage and access directly for efficiency and optimal read and write performance.
A file system defines how data is organized and stored as files and directories on IO devices. It provides a hierarchical structure for applications and users to easily access and manage their files based on permissions. A distributed file system improves scalability, fault tolerance, and performance by partitioning and replicating data across multiple networked machines.
Motivation: Every application needs an efficient and secure abstraction over the raw bytes in storage devices. File systems provide such an abstraction for applications in databases and operating systems.
IO Algorithms show code for sorting, hashing, indexing, and joins. These algorithms are used to process the DbFiles and perform various operations, such as sorting the data for efficient querying, building indexes for faster lookups, and joining multiple tables together.

Motivation: While readers will be familiar with classic algorithms that work on data in RAM, we will focus on algorithms that work with ``big data’’ that do not fit in RAM. For instance, BigSort, an extension of classic sorting algorithms, operates on DbFiles and can scale to petabytes of data, unlike traditional RAM-based sorting algorithms limited to gigabytes of data.



Case Study 6.1
How data apps store tables in IO devices?
Goal: Learn how tables are stored in IO devices


In this section, we discuss how to store Spotify’s tables (Users, Songs, Listens, etc.). With that in mind, let's take a closer look at how to optimize storage and scale for your data needs.

Figure 1: Paging on a basic machine
Definitions
IO paging: When a CPU wants to read data from RAM, it sends a read request to the RAM controller, which retrieves the requested data from RAM and sends it back to the CPU. When the CPU needs to access data that is not in RAM, it sends a request to one or more IO devices, which retrieves the data from those devices and sends it to RAM. The CPU can then access the data from RAM as usual. This process is known as paging and is used to manage the limited amount of RAM available in a system.
IO throughput and access latency are two important factors to consider when choosing a storage medium for a given data set. Throughput refers to the amount of data that can be transferred in a given time period, while access latency refers to the time it takes for the CPU to receive the 1st byte of data for an IO request.
Example: In Figure 2, we see example access latencies and throughputs for different IO devices. In general, SSDs have higher throughput and lower access latency than HDDs. This is because SSDs use NAND flash memory, which allows for faster IO operations. On  the other hand, in a HDD, we use mechanical disks that physically spin (like old gramophone records) and it takes much longer to access the right location (also called a ‘’disk seek’’) on a mechanical platter. SSDs also cost more, and have a limited number of write cycles before they can no longer be used, making them less suitable for applications that require frequent write operations. RAM has the highest throughput and lowest access latency of any storage medium, but it is also volatile memory, meaning that data is lost when the power goes out. Additionally, RAM is much more expensive than HDDs or SSDs, making it impractical for most big storage applications. Append operations are more efficient in HDDs than writes since HDDs can directly append data. 
IO pages (or blocks) : When performing IO operations, reading and writing a single byte from an IO device can be costly. To amortize this cost, we perform bulk operations on IO pages, which is a fixed-size unit of data, typically 64 MBs, that is read from or written to an IO device during IO operations. 
Motivation: This is akin to how Amazon’s vans deliver batches of thousands of packages to our streets from the warehouse, rather than delivering them one package at a time. 


 
Figure 2: Summary of access times and throughput for IO devices
IODevices

In Section 1 of the NanoDB Colab, we discuss IODevices. Specifically, we work through example code for IO cost models for reading and writing from different IO devices. 

Here we see three example IO devices - ram1, ssd1, and hdd1 - with different access times, and scan speeds. The ssd1 device, for example, has an access time of 10 microseconds, a scan speed of 5 GBps, and a write cost of 1.0. In this example, we set C_w (the write cost relative to a read) to be 1.0. In practice, C_w ranges from 1.0 to 10.0 based on the IO device.

The read_pages_cost function is a method that estimates the time required to access and scan a certain number of data pages from an IO device. The calculation takes into account the device's access time, page size, and scan speed. The result is the total time it takes to complete the read operation, expressed in seconds. 

This is a simplified IOcost model that provides a good approximation of the cost of reading data pages from an I/O device.

Let’s first calculate the size of the Songs table when we have 500 million songs. The size of each row in the table is 64 bytes (int64) plus the average size of the title, name, and genre columns. We assume an average row size of 1024 bytes and pageSize = 64MBs. We see that Songs uses 488281.25 MBs, and can be stored in 7630 pages. 

Also we see the time to read 100 pages using the ReadPages() method from different IO devices. RAM takes ~0.06 secs, and HDD takes ~65 secs.

Cloud data centers
Cloud data centers provide a scalable and cost-effective solution for storage and processing of large amounts of data. By leveraging the above mentioned storage IO devices, cloud providers can offer a variety of options for storing data, from high-performance SSDs to cost-effective HDDs. Additionally, with good distributed computing software, data centers can parallelize reads, writes, and queries across multiple machines, allowing for faster data processing. 
Takeaways
Know the performance of your IO devices and file systems, where your data is stored
File systems offer files as a simple and useful abstraction over raw storage in IO devices


Case Study 6.2 
How NanoDB stores rows into DbFiles?
Goal: See how a toy database stores and manages rows of data in a file system 

NanoDB uses DbFiles to represent tables, such as Songs, where each table consists of rows and columns. By default, we divide the set of rows into a series of pages on the file system in an IO device. This approach is commonly referred to as a row-oriented store or a row store. In a later section, we'll also discuss column stores (where data is organized by columns). 





In this example, we have a logical table Songs with 100 songs and information about the songs.

The corresponding physical table Songs has 100 rows (one row per song) and columns (for song ID, song name, etc.). In this example, say each page can hold three rows. Song's data is then physically stored in a DbFile with 34 pages. In our visual representation on the left, we see the DbFile name (Songs), number of pages (34) in the DbFile, and each of the Pages stored in the DbFile. 

For example, consider the 0th page, which contains 3 rows – [(188, ‘kg’, ‘..’), (492, ‘oa’, ‘...’), (359, ‘cl’, ‘..’)]. The row (188, ‘kg’, ‘..’) represents the 0th row of the Songs table with the song ID (188) and other song details (abbreviated to ‘kg’, ‘..’), and is stored in the 0th page. Similarly, (492, ‘oa’) represents the next row, and so on. The last page contains the row (17, ‘oa’, ‘..’), with enough space to accommodate two additional rows (marked as ‘None’). 

Similarly, Listens has 100 rows, and is stored in a DbFile with 15 pages, each capable of holding 7 rows. These are examples. In practice, the number of rows depends on the row sizes in each table, and any ‘free’ space we want to leave in pages for new data.

In the NanoDB Colab, you can play with different row sizes and columns

Example File System
Google’s Colossus file system is a distributed file system that is designed to store and manage large amounts of data (for Youtube, Gmail, etc.) across a massive cluster of machines. The file system is built on several key principles that enable it to provide high-performance, fault-tolerant data storage and access, including
Data partitioning: Colossus' file system partitions data into small, fixed-size chunks called blocks, similar to the pages in DbFiles.  Each block is typically 64 MB in size.
Distributed metadata management: Colossus' file system tracks where each block is stored and how it can be accessed. This metadata is stored separately from the data itself, and is replicated across multiple machines for fault tolerance.
Replication and redundancy: Colossus' file system uses replication and redundancy to ensure that data is always available, even in the event of a hardware or software failure. Each block is typically replicated across three (or more) machines, and the system automatically detects and replaces failed machines to maintain redundancy. While reads can read from any of the replicas, writes will need to update all the replicas, and that could make it more expensive. 
Case Study 7.1 
NanoDB’s Algorithms for Hashing and Sorting

Goal: Learn how to build efficient IO algorithms for Hashing and Sorting big data

We saw how to store the Songs table in NanoDB’s DbFiles. However, if we want to search for a specific song ID, it would be inefficient to read and check every page in the Songs table. 
For instance, if we have a row that contains data for a song, such as song ID, name, artist, and other details, and we want to index the data based on the song ID, we can create a (song ID, value) pair. Here, the song ID will be the key by which we can search and retrieve the rest of the data associated with that particular song. 

In general, these rows are known as search key-value pairs or key-value pairs. The key serves as a search criterion, and the value is typically the remaining row data. Recall there are two kinds of key-value pairs
A primary key is a unique identifier and has no duplicate values. For example, in the above Songs table, song ID serves as a primary key, which means that it uniquely identifies a single row in the table, mapping to a specific artist and song.
A secondary key is a non-unique identifier and could have multiple values associated with it. For example, we may want to search for a specific artist, where artist is a secondary key, but that can map to multiple song rows. 
To speed up search, we next discuss how to partition DbFiles using hash partitioning, and cluster data using sorting.
Hash partitioning for IO devices and machine clusters
Recall how basic hashing works for strings. E.g., given names = ['Alice’, 'Bob', ‘Charlie’], we can use tools like python’s built-in `hash()` to convert each string into a unique integer. To hash more complex types like stock ticker and date, we can use python’s hashlib.sha256(ticker+date). We can use the resulting hash values to build an index structure that allows fast lookup of equal (or similar) values. With a RAM-based hash table, we can perform constant time lookups on average. 
For big data, we’ll often use a "disk-based hash table." In this approach, the hash table is broken up into multiple "partitions," and each partition is stored as a separate file on disk. For a new key-value pair, the hash function is applied to the key to determine which partition the pair belongs in. The key-value pair is then appended to the end of the corresponding partition file. 
When we need to find a value, the hash function is applied to the value to determine which partition it belongs in. The corresponding partition file is then loaded into memory, and a linear search is performed to find the key-value pair with the matching key. 
Hashing can also be used for partitioning (also known as sharding) data across multiple machines in a parallel computing environment. The basic idea is that each piece of data is hashed to produce a hash value, and this hash value is used to determine which machine in the cluster should store the data.
For example, if we have a set of data that we want to shard across one hundred machines, we could use a hash function to map each data point to a value between 0 and 99 (inclusive), and then store all the data points that hash to the same value on the same machine. This way, each machine is responsible for a roughly equal portion of the data, and we can distribute the workload across multiple machines to speed up processing.
In practice, there are many different ways to shard data using hashing, and the specific method used will depend on factors such as the size of the data set, the number of machines available, and the distribution of the data. 

Hash-Partition uses a hash function to break a relation into smaller partitions, using a given amount of B (buffer pages) in RAM. (It uses an extra page for input data, and uses B for output pages.)

In Step 1, HP(Songs) sets up B DbFiles to store the outputs. In Step 2, it reads each page into RAM (one page at a time). Each value is hashed, and appended to the corresponding partition. When one of the B partitions becomes full, the page is appended to the output partition on the IO device (e.g., SSD or HDD), freeing up space in the buffer for additional values to be hashed.

For example, we see four output partitions (B =4) in RAM, and four output partitions in disk (Songs.0, Songs.1, Songs.2, Songs.3).  (For this example, we only show Songs.1’s pages.) When we read in one input page with rows for 320, 101, 197, the rows for 320 and 101 get hashed to partitions 0 and 1. At this point, the output page for partitions 0 and 1 are full. These pages are appended to Songs.0 and Songs.1, and their buffer space is cleared. That is,
Page [(305, ‘hp’, ‘..’), (489, ‘uc’, ‘..’), (101, ‘ya’, ‘..’)] will be appended to Songs.1. (And [(168, ..), (80, ..), (320, ..)] to Songs.0)
(197, ‘rm’, ..) in the input page will get mapped to partition 1. 
And then the next input page is read. 
With this algorithm, we only need buffer space for one input page and B output pages, one for each partition. (Independent of the size of the input table, P(R), that needs to be partitioned.)

We’ll discuss IO costs and complexity shortly. (As a preview, if P(R) refers to the number of pages in table R, notice that Step 2 will cost us P(R) (we read each of R’s pages once). Also, Step 3 costs us P(R). We produce the same number of pages as the input, after hashing.) 

For example, let’s hash-partition Songs into four partitions (stored in DbFiles Songs.0, Songs.1, Songs.2, Songs.3). For this, we use a hash function to map each row value into one of the four partitions. E.g., song IDs 188 and 359 map to Songs.0 and Songs.3. In Songs.0 we see that song ID 188 is in page #0, and song ID 168 is in page #2 of the Songs.0 partition. 

If a query wants to find the row associated with song ID 168, we apply the hash function to pick the specific DbFile (Songs.0) to retrieve the needed row. If a query wants to find value=193, we’ll check Songs.2 (e.g., hash(193) maps to Songs.2). It’s not present in Songs.2, and so cannot be in Songs. 

Partitioning the Songs table helps narrow down the search space and make it easier to find the desired song ID. This is especially useful when dealing with big datasets. By dividing the data into smaller subsets, we can parallelize the processing and reduce the search time. Hash-partitioning is a common technique used in distributed systems to ‘’divide and conquer’’ data across multiple nodes for parallel processing. However, notice that we are still doing linear search, inside a partition of pages.
Sorting big data using disks and machine clusters
Sorting is another common approach to organize big data sets. Common sorting algorithms like quicksort and mergesort are used to sort lists of integers in RAM, to efficiently search and build additional data structures. We discuss techniques to extend these ideas to big data sets.  
To sort big datasets, we can use a technique known as BigSort or external sorting. In the first step, we divide the large dataset into smaller chunks that can fit into RAM, sort each chunk using an efficient algorithm, and then write each sorted chunk to disk. In the second step, we merge the sorted chunks into a single larger file using a merge algorithm that efficiently combines the chunks into a final sorted file.
When working with machine clusters, we can further optimize sorting by distributing the workload across multiple machines in the cluster. This approach is called distributed sorting and involves breaking up the dataset into partitions and distributing the partitions across multiple machines in the cluster. Each machine sorts its partition independently, and the sorted partitions are merged to produce the final sorted dataset. This approach is highly scalable and can handle big datasets.
 

The BigSort method sorts a big file that does not fit in RAM. It splits the big file into many small files, sorts each small file in RAM, and uses mergeBway to merge B sorted files at a time. 

Overall, by breaking down the sorting process into smaller pieces, we can more easily manage and sort large datasets efficiently.



The mergeBway method implements a merge sort algorithm to merge B partially sorted files into a bigger sorted file. In Step 1, the method reads the first page of each file and creates a heap to track the values and which file/page they are from. In Step 2, it repeatedly selects the smallest value from the heap, appends it to the output file, and reads the next value from the file associated with the value just appended, adding it to the heap.



Let's go through an example of sorting Songs with B = 4 to gain a better understanding of the process.

Step 1: We'll start by breaking Songs into smaller chunks and writing sorted DbFiles (Songs-0-0 to Songs-0-8) with up to B (=4) pages each.

Step 2: Next, we'll merge the DbFiles to create larger, sorted files. In the first run of mergeBway (run = 1), we merge B (4 in this case) DbFiles at a time to produce sorted DbFiles (Songs-1-0 to Songs-1-2) with up to B^2 pages.

Step 3: We continue merging until we have one fully sorted DbFile. In the second run, we merge B DbFiles from run=1 and produce a sorted DbFile (Songs-2-0). If Songs were larger, we would continue this process for each subsequent run (Songs-i-0 to ...) until we have one fully sorted file.

In the NanoDB colab, you can try the larger Songs100x file (or make your own), to see how the merge steps happen for much bigger data sets.


BigSort Listens table on “songID” (visual) 

Input: Listens table with 7 rows per page. RAM Buffer: B=4 pages
Goal: BigSort table of 58 pages, using only B=4 space in RAM.

Here’s a visual layout of BigSort for intuition. We only show the sort values (song ID in this case), and use light blue for small values and dark blues for big values (along with the values in text), to make it easy. For example, notice the input table has a mix of light and dark blues in random spots. The final sorted output has the values organized from light to dark.

Split into B-page files
# 1. Split big file into many small files of B pages each
#    2.     Sort each small file (in RAM). Write sorted output below.
# Color code: Focus on purple boxes in (above) and below. 1st B pages (above) are sorted and written below. Repeat for next B pages (in dotted purple).

# Merge B sorted files into bigger files. Repeat until done.
# Color code: Focus on red and green. Read the 1st page of 1st B files(red boxes) to merge. Read extra pages (green) to check if there may be smaller values, before writing sorted values in the next step. Notice that 80, 81, 93, 95 (in green) were read in from the green (2nd pages), while 122, 128, 132 and 138 (from the 1st pages) had to be written after the green values were written. 

# Merge pass 2 and final output



Case Study 7.2
How NanoDB models IO costs?

Goal: Learn how to model IO costs for reading and writing data stored in IO devices


IO Complexity
Consider the example of running QuickSort on ‘n’ integers stored in RAM. The computational complexity is O(n log n) in CPU. 
Computational (or CPU) complexity is a fundamental concept in computer science algorithms, which measures the cost of CPU operations required to solve a problem. It provides a theoretical understanding of how algorithms perform on inputs of different sizes and is often used to compare the efficiency of different algorithms. However, computational complexity is just one aspect of a larger picture of systems complexity.
System complexity refers to the complexity of the entire system involved in a particular computation, including hardware, software, and network components. It includes not only computational complexity but also factors such as I/O complexity and network complexity, which are crucial in large-scale distributed computing systems.
For example, consider the shuffle operation in a distributed system. The shuffle operation is used to distribute data across nodes in a cluster. The computational complexity of the shuffle operation itself is relatively low. However, the IO and network complexity involved in shuffling large amounts of data in reading data from disks, and across the network can have a significant impact on the performance of the entire system.
In big data systems, we focus on IO complexity, which refers to the amount of data that needs to be read from or written to disk during the execution of a query, because reading or writing data to disk is much slower than processing data in memory. 
Aren’t computational complexity and IO complexity both a factor of data size? Why make a distinction? Computational complexity and I/O complexity are both closely related to data size, but they also have some differences that can impact system performance. Let’s use a real-world analogy from food delivery apps to help illustrate these differences. 
Imagine picking up ten food delivery orders, considering the pickup time (the time it takes to walk out with your pickup order) and the drive time to the restaurant. When the restaurants are located within a short walking distance on a single street like University Ave, the pickup time (akin to “computational complexity”) would be the primary cost. However, if the orders are spread across five different streets (e.g., in California Avenue and Castro Avenue), the drive time and parking (akin to “IO complexity”) would be the dominant costs. In both cases, we are picking up 10 orders, but the costs differ.    
The main intuition when analyzing IO costs of our algorithms is to (a) count the number of pages read from disk to RAM, and (b) multiplying it by the read cost, C_r. Similarly, count the number of pages written from RAM to disk, and multiply by the write cost, C_w. For table R, use T(R) to represent the number of rows in R, and P(R) for the number of pages in R.  


The IO costs for various algorithms are summarized in the Figure. We have also provided simplified formulas for common cases. These are easy to derive from the general formula. 

For example, when N < 2B and C_r = C_w = 1, Sort(R)’s IO cost = (1+1)*N*(1 + 0) = 2N. (ceiling of log of a number between 0 and 1 is zero). 

Also, see examples on how these formulas can be applied to specific problems.



Intuition for above formulas (Optional)

In HashPartition’s Step 2 we read each of R’s pages once. That is, it costs us C_r*P(R). Also, in Step 3 we write P(R) pages, because we output the same number of pages as the input, after hashing. This step costs us C_w*P(R). The overall IO cost is then (C_r + C_w)*P(R). 
Here’s the intuition for the BigSort(R) method:
In the first pass, the big file is read and split into smaller files, which are sorted in RAM. This involves reading the entire big file and writing the sorted smaller files back to disk. The I/O cost for this pass is (C_r+C_w)*N, where N is P(R), the number of pages in the big file.
In the mergeBway method, merging is done in multiple passes. In each pass, the method reads B input files and writes a single output file. The I/O cost for each pass is (C_r+C_w)* N), as N pages are read (overall) from the B input files and written to the output file. Also, we’d need log_B(N/B) passes to merge all the smaller files into a single sorted file.  
Big sorting (also called external sorting) is an important and popular problem with many optimizations. One popular optimization is called “repacking,” a version of sorting where we keep additional information to reduce the number of writes. In the case where the input data is nearly sorted, intuitively, this optimization reduces the amount of work that needs to be done during the merging phase, since many records are already in the correct sorted order. We can then minimize the number of comparisons and swaps required to merge the chunks into a final sorted output.
Overall, the repacking optimization can help improve the performance of external sorting when the input data is nearly sorted. It's one of many clever techniques that takes advantage of the inherent structure in the data to minimize the amount of work required to sort it. In general, we get the extra factor of 2 in the denominator in log_B N/2B from such optimizations. 



Case Study 8
How NanoDb indexes data to speed up searches?
Goal: Learn how to build indices for fast search over data


Definitions
Hash Index: A hash index is a data structure that maps keys to their corresponding row’s locations in a page using a hash function.

Motivation: Quickly locate records in a table by calculating a hash value for a given key, which directly points to the record's location.
B+ Tree Index: A balanced tree data structure that maintains sorted data in a hierarchical manner, with leaf nodes containing actual records or pointers to them.

Motivation: Facilitate efficient search, insertion, and deletion operations by organizing data in a tree structure that allows for quick navigation to the desired records.
Hash Index/Sorted (when underlying data is sorted): Optimizes a hash index when data rows are sorted by indexed key, where records sharing the same hash value are stored together.

Motivation: Improve query performance by leveraging the speed of hash indexes while maintaining the benefits of sorted data, such as faster range queries and reduced storage overhead.
B+ Tree Index/Sorted: Optimizes a B+ tree index when data records are sorted based on the indexed key.

Motivation: Enhance query performance by combining the search efficiency of a B+ tree with a more compact index, and reduced I/O operations and faster retrieval..
Online vs. Offline Index: An online (or incremental) index is built incrementally as data comes in, whereas an offline (or batch) index is built after all the data is available at once.

Motivation: Online indexing provides immediate access to the index as new data arrives, enabling real-time querying, while offline indexing allows for optimized index construction on a complete dataset, potentially resulting in a more compact and efficient index.


NanoDB’s IndexFiles
IndexFiles are a special type of DbFiles. Each page in an IndexFile contains rows in the form of (value, datapage#). These rows give us a map of the data page number where we can locate a specific data value. IndexFiles are often called Indexes or Indices. (This is intuitively similar to how “pointers” in RAM data structures are memory addresses. I.e., location of what we are pointing to) 


Pointers are “really” memory addresses. E.g.,  linked list a → b → c is really [a, 0x100], [b, 0x210], where 0x100 is b’s address. That is, each item knows the location of the next item. (i.e, has a virtual pointer). 

We use dotted arrows to refer to a virtual pointer, and address to refer to physical representation

Similarly, the HashTable’s [45, 83] 
indicates the data row for songID=45 is in page #83. Similarly, [578, 65] indicates we can find the row for songID =578 in page #65. (I.e., a virtual pointer to identify which page a data row is stored in.) 







For example, let’s build an index for the Songs table, and store it in Songs.idx, an IndexFile. This is a basic index (or Hash index) that tracks song ID to the page numbers in the Songs DbFile. That is, (14, 15) in Songs.idx means that songID = 14 can be found in page# 15 of the Songs DbFile. Note that we keep the song IDs sorted in Songs.idx (by default).

In this example, observe that each page of the Song table has 3 rows, while the Song.idx has 14 rows. For instance, the Songs' page #0 contains [(188, 'kg', '..'), (492, 'oa', '..'), (359, 'cl', '..')], while the Songs.idx's page #0 has [(14, 15), (17, 33), … (80, 12)]. Despite having the same page size (e.g., 64 MB), more index rows can fit compared to data rows. This is because data rows require more bytes to represent the complete data row, while index rows only store the (value, page #) pair.



MakeBasicIndex creates a basic hash index for a DbFile. The function performs the following steps:
Read each page in a DbFile.
For each value in the page, add (value, page number) to the index.
To query the index for a needed value, scan the index to find the page# with the value. If the value is not found in the index, the value is not in the data.
By default, we keep the index sorted by song ID, for search.



When we perform a query on Song.idx (using QueryIndex), we walk through each page in Songs.idx (sorted by default), and check if what we are searching for (e.g., song ID = 80) is present in Songs.idx. In this case, we find a tuple (80, 22) in Songs.idx. This implies song ID = 80 is in page# 22 in Songs’ DbFile. (You could also extend this version by doing a binary search amongst the index values.)
  

B+ tree index



Next, let’s build a B+ tree index. This is a multi-level index structure, where each level is a sorted index of the next level. These multi-level indexes allow us to scale to even bigger datasets.

To create a B+ tree index with MakeBPlusTreeIndex, we start by building a basic index of the table and then recursively create sorted indexes of the previous level until we reach a level with only one page, the root of the tree.  

In Songs.idx’s page# 0, we see index entries (14, 15) and (17, 33), which tell us that song ID 14 is in Song’s data page 15, and song ID 17 is in Song’s data page 33. In B+ trees, we index Songs.idx further. This involves treating Songs.idx as another DbFile, and creating a Songs.idx.idx file for it.





When we want to search for a specific value in the B+ tree index with QueryBPlusIndex, we start at the root level and walk down the tree to the leaf node. At each level, we use the sorted index to find the appropriate page to search in the next level. Once we reach the leaf node, we read the data page using the page number obtained from the leaf node index.

Overall, the B+ tree index allows for efficient searching of values in the table, with the number of disk accesses required proportional to the height of the tree.

To search for song ID = 166 in Songs, we first read page#0 in Songs.idx.idx, and find (166, 2). Next, we read page# 2 in Songs.idx, where we find (166, 25). We finally read page# 25 from Songs to retrieve the row associated with song ID 166, which is (166, 'aa', '..'). 

Let's consider an example where we want to find multiple users listening to the same song ID. In this case, we would index the Listens table on song ID, but we can have duplicate song IDs in Listens since multiple users can listen to the same song ID. The B+ tree index can handle duplicates, as shown below.

To find the song ID = 166 in Listens, we would locate (127, 2) and (196, 3) in Listens.idx.idx, like earlier. Next, we would read page #2 in Listens.idx to find (166, 12), which would direct us to read page #12 in Listens and retrieve the row for song ID 166.

Additionally, observe that song ID = 14 has two entries, (14, 1) and (14, 9), in Listens.idx. These entries correspond to two separate data rows associated with two users listening to the same song ID. We can find these data rows in pages #1 and #9 of the Listens table.

Optimizing Hash indexes with Sorted data rows 




When creating an index for a sorted DbFile, we can optimize our index to be more compact. Consider Songs-2-0, the sorted version of Songs, where the DbFile is sorted by song IDs. 

For example, in Songs.idx we see the 1st few index rows are (14,0) and (21,1), where the first value is the song ID and second value is the data page#. We do not explicitly keep entries like (17, 0) because we know that if it exists, it has to be in page#0 in Songs-2-0.

As a result, we see that Songs.idx is now only 3 pages compared to the 8-page index we created earlier. This is because we only track the first value in each data page.
 
An index over sorted data is also known as a Hash Index/Sorted (also Clustered Hash Index).  In MakeIndexForSortedData, we show sample code for building such an index. Notice that our QueryIndex code will work on this index as well.

Clustered B+ tree indexes

Sorted Listens


B+ index over sorted Listens



Clustered B+ tree index on sorted Listens


Similarly, we can build a B+ tree/Sorted (aka Clustered B+ Tree) index. This index allows for both exact and range searches. For example, if we sort the Listens table by song ID (and store it in Listens-1) and create a clustered B+ tree index, we can optimize searches for song IDs. 

Compared to the basic (unsorted) B+ tree indices, such indices are more compact. For instance, in case (a), the regular B+ index (``unsorted’’) on a sorted Listens table, page #0 of Listens.idx tracks data rows for all song IDs between 3 and 54. In the sorted version (c ) of Listens.idx, we take advantage of the sorted data and can determine that song IDs in the ranges [3, 22) and [22, 58) are only found in pages #0 and #1, respectively. Hence the clustered index uses only 2 pages versus the 8 pages for the regular (unclustered) version.

When searching for song IDs 9 and 10, the regular Listens.idx tells us that song ID 9 is on page #0, and there is no row for song ID 10. In contrast, with the clustered Listens.idx, we need to read the data page (i.e., extra IO) to verify the existence of the song ID. However, for most queries, accessing the data page is necessary anyway.

Such sorted indices also facilitate range searches. To find all rows with song ID greater than or equal to 400, we can consult Listens.idx and see that associated rows are located in pages 10 to 14 of the sorted Listens table. We can then scan just those data pages to find all the relevant data.

Overall, when we can sort the underlying data by the search values, such sorted indices are a popular and compact option for optimizing searches for big data sets.



Often, we find it useful to represent a B+ tree visually as a tree. Here’s an example of the above B+ tree/sorted for the sorted Listens table. 

This B+ tree index has two levels – the root (on top representing the pages in Listens.idx.idx) and the leafs (Listen.idx). In general, a B+ tree can have more levels.

We use dotted lines to indicate the next page # that has the next pointer to follow (i.e., the page # to read next). For example, 432 in root points to the leaf node (432, 450, …, 499). And 432 in the next level points to the page at the next level, and so on. 

In addition, at the bottom of the tree are the data pages for sorted Listens. For example, we see data page #0 is [(14,’nc’, ‘..’), (17, ‘oa’, ‘..’), (18, ‘ix’, ‘..’)].  




The index fanout (or fanout 'f') represents the maximum number of (search_key, page#) pairs that can fit within a single (index) page. It is calculated using the size of the search_key and the pointer size (number of bytes to store the page#). For instance, in the Listens example, we'd likely use (8 bytes, 8 bytes) for the (song ID, page#) pair. That is, fanout <= page_size/(search_key size + pointer size). (We take floor() in the equation on the left, because fanout has to be an integer. You can’t have “47.2” number of pointers.)

In a B+ tree, each node at level i can point to 'f' nodes at the subsequent level. For example, the root (at level zero) contains 'f' search_keys and can point to up to 'f' nodes on the next level. Thus, the number of nodes at each level follows the sequence: 1, f, f^2, ..., f^i, and so on. The last level will have f^h pointers and f^{h-1} nodes, for a B+ tree of height ‘h’. (Trivial case: h = 1, implies only root node. Note because this trips up students early on – for height ‘h’, nodes are at levels 0, 1, ..h-1)

For simplicity, let’s assume the leaf nodes must be able to point to each of the num_search_keys within the corresponding data pages. For example, if we need to index 1 million data rows, we’ll assume the leaf nodes have to point to 1 million search keys. (In practice, we could optimize further if the data is sorted, based on how many distinct search keys there are, etc. Let’s keep it simple for now.) 

That is, f^h >= num_search_keys. The index height ‘h’ for such a B+ tree is calculated as demonstrated in the code. Observe that when conducting a search, we only need to traverse the height of the B+ tree. Assuming no data is cached, the height represents the maximum number of IO operations required to perform an index lookup. 

In addition, we may need an extra IO to read the data page for the actual query. For example, if we build an index on song_id, we’d traverse the above index to find the data rows for song_id. Finally, if the query needs [song_id, name, artist], we’d find the relevant data row(s) in the data page(s). So we’d do an IO, if necessary, to read that data page. If the query only does a COUNT(song_id), then we don’t need to read the data page. 


In this example, we examine two scenarios with different page sizes (64 KB and 64 MB) while varying the number of search keys and search key sizes.

For a page size of 64 MB and 1 million song IDs using 8 bytes for each song ID in the Listens dataset, the fanout is 4,194,304, and the tree height is 1. For 1 trillion song IDs we can locate a song ID with only 2 I/O operations for the index (root + leaf). 

We could also build indexes on our compound search keys, such as
(song ID, artist ID, album, release year, …) versus just song ID. We see an example where the search key size is 1,024 bytes to model such compound keys. Although the fanout decreases, we can still index 1 trillion search keys within 3 levels of a B+ tree.

Lastly, for educational purposes, we investigate how the height changes when using a smaller page size (e.g., 64 KB). Here, we see variations in the tree height. In practice, B+ trees are powerful because we have big page sizes, and we can fit a lot of search keys into the page. 

In summary, the key insight is that B+ trees enable quick index lookups with just 2-3 I/O operations on disk, providing an efficient search index for big data.

In this case study, we learned about two broad techniques to efficiently search large datasets: partitioning and building various indices such as Hash Index, Hash Index/Sorted, B+ trees, and B+ trees/Sorted. These techniques are independent and can be combined in different ways to solve specific problems. For example, we can partition data to break down a big dataset into smaller subsets and then build a Hash Index, or a B+ tree index on each subset to speed up search.
Case Study 8.1
How do UberEats and Google Maps speedup geo queries using hashing in RAM? 
Goal: Learn how to build indices on multidimensional data


In food delivery and mapping applications, it’s important to optimize the travel times and cost. Consider how to group ``nearby’’ orders together and assign them to the same delivery driver. For example, let’s say we have a list of orders with the following locations in latitude, longitude: orders = [(37.788022, -122.399797), (37.788122, -122.399797), (37.788022, -122.398897)]. 
Geo data often involves searching for points that are near each other in two dimensions: latitude and longitude. To accomplish this, we need to extend our hashing and sorting techniques beyond the one-dimensional search key, such as a song ID, to account for nearness.. 
In the next two subsections, we dive into the mathematics of hashing, and extend our sorting, partitioning and indexing techniques from the last section, to multi-dimensional search keys. We can also play with  these examples in the Hashing colab. 
Geo hashing is one such method for encoding a geographic location into a short string of letters and digits. First, we divide the earth into a grid of squares, with each square being identified by a unique geo hash. Next, we divide each square into smaller squares, and repeat the process until we reach a precision of our desired geo hash length.  For example, consider geo hashing (37.788022, -122.399797). In this case, we'll use a geo hash length of 5 characters, which gives us a precision of about 2.8 km. The resulting geo hash for the location (37.788022, -122.399797) would be "9q8yy". This geo hash can be used to quickly retrieve the location coordinates and also to find nearby locations with small variations of the hash.


Hexagon-based hashing using H3 cells is a recent and more powerful method for encoding a geographic location into a short string of letters and digits, similar to geo-hashing (and Google’s S2 cells). H3 cells are a hierarchical grid system that uses hexagons to divide the earth's surface into cells of various levels of resolution. It is an open-source library developed by Uber.



This code snippet shows how to use the h3.geo_to_h3 function to convert latitude and longitude coordinates into hexagonal cell IDs for a given zoom level. The example includes the coordinates of four locations: SF Mission, and three buildings on Stanford campus (Nvidia Auditorium, Packard and Gates buildings).

At zoom level 8, all three Stanford locations map to the same cell ID. At zoom level 12, Packard and Gates, which are close to each other, differ only in the last three characters of their cell IDs. Similarly, NVidia differs from the other Stanford locations only in the last five characters of its cell ID, while SF Mission, which is further away, has a unique cell ID. Uber Eats (and each geo app) picks one or more zoom levels for hashing, based on the use case and the required precision.

Extending Hashing to more domains
PhotoDNA (from Microsoft), a perceptual image hashing tool, helps detect and prevent the distribution of child sexual abuse material (CSAM) on the internet. The technology creates a unique hash for an image, which can then be compared to other images' hashes in a database to identify and block known CSAM content. PhotoDNA is widely used by online platforms and law enforcement agencies to combat the proliferation of CSAM. The generated hash is robust to minor alterations like resizing, compression, and color changes. While Microsoft doesn't provide a public API for PhotoDNA, they offer the technology to select organizations involved in combating CSAM. However, there are open-source implementations of similar perceptual hashing techniques (e.g., imagehash)
Hashing DNA sequences can help convert a DNA sequence into a fixed-size representation, similar to how a hash function works. One way to hash DNA sequences is to use a technique with window hashing. Window hashing is a method of breaking a DNA sequence into overlapping substrings of a fixed length (k), and then using a hash function to convert each substring into a unique hash value. For example, if k=4, the DNA sequence "AGCTAGCT" would be broken into the following substrings: "AGCT", "GCTA", "CTAG", "TAGC", "AGCT". These substrings are then hashed using a hash function such as SHA-256 to produce a unique hash value for each substring. 
In summary, we saw techniques to map complex data types into hash values, which can be used for partitioning and indexing. For example, we can use H3 to convert a set of Geo Points (latitudes and longitudes) into hash values, and then index the points using the hash value. By combining these hashing techniques, we can efficiently store and retrieve large amounts of data while minimizing IO operations and improving overall performance

Case Study 8.2
How do OpenAI’s apps and Facebook’s AI speedup queries using vector databases? 
Goal: Learn how to build efficient approximate indices for very high dimensional data

Often, applications need a cheap way to compute approximate nearest neighbors (ANNs) in high-dimensional spaces. For example, OpenAI uses text embeddings to represent semantic connections between textual data, utilizing vectors with thousands of dimensions, to find and generate text that’s similar to a vast index containing billions of documents. In such applications, classic hashing-based indices to find exact matching results are not sufficient. 
Vector databases are specialized databases designed to efficiently store and query high-dimensional vectors (e.g. OpenAI's embeddings), which are often used in various machine learning and natural language processing tasks. These databases use similar indexing techniques as our prior indexing techniques, but enable fast similarity search and nearest neighbor queries in large datasets, even in high-dimensional spaces. ANN algorithms offer a fast and efficient way to find similar vectors in high-dimensional spaces without an exhaustive search. 
FAISS (Facebook AI Similarity Search) is one such library designed for efficient similarity search and clustering of dense vectors. While our prior hashing based indices supported exact lookups, FAISS supports various distance metrics to measure similarity between vectors, including Euclidean (L2) distance, and dot products. Also, FAISS can leverage GPUs to speedup indexing and search operations.
First, let’s see how FAISS helps us find approximate nearest neighbors for a 700+ D space for text embeddings, like in OpenAI’s GPT for text data.


…
Sample text embedding for “String 42 is making me thirsty.”





In (a), we have an example of a text embedding represented as a 768-dimensional vector using the popular AI model, Sentence-BERT.

In this example, we first embed 100 strings into FAISS's vector index. Then, we query for three different strings to find the approximate nearest neighbors. The top 5 results and the distances from the query string are displayed.

Observe that "String 42 is making me hungry" has an exact match. Additionally, it discovers other related, similar strings nearby in this 768-dimensional space.

Similarly, “String 42” and “String 42 is making me thirsty” do not have exact matches, but match with similar strings.

 

Next, we see how Locality Sensitive Hashing (LSH) helps us index and query a set of points in a 5000 D space of vectors, and in a 256 D space for image embeddings. We can also play with these examples in the Hashing colab. LSH offers sublinear-time similarity search, trading off some accuracy for speed. 



In this first example, the IndexLSH object is trained on the set of points, and then used to find approximate nearest neighbors for a new query point. The k-neighbors method returns the indices of the approximate nearest neighbors in the original set of points.



In this example, we see how we can map images to a 256-dimension vector, and use these vectors to index and query data. 

Intuition for how Locality Sensitive Hashing works
The main idea behind LSH is to hash input items (like vectors) in such a way that similar items have a higher probability of being mapped to the same hash bucket, while dissimilar items are likely to be mapped to different buckets. We can generalize the principles behind our prior hash indices, as follows.
Pick a family of hash functions that are sensitive to the distance metric used for measuring similarity between input items (e.g., Euclidean distance, dot products). These hash functions have the property that the probability of two items having the same hash value is proportional to their similarity.
Construct multiple hash indexes with randomly selected hash functions.
Query by computing hash values, retrieve items from corresponding buckets, and measure similarity. We can reuse principles from our prior indexing techniques in managing and querying from these buckets on disk for scale.

Case Study 8.3
How Spotify supports search on text?
Goal: Learn how to build indices on text data for fast text search

Spotify uses inverted indices for text search by creating an index of all the words in the metadata associated with each track, such as the song title, artist name, album name, and other relevant tags.
Inverted indices are useful because they allow for efficient text searching in large collections of documents. Traditionally, text searching involves scanning each document in a collection for occurrences of a search term, which can be slow and expensive for large collections. Inverted indices offer a more efficient alternative by pre-processing the documents and creating an index of all the words or terms contained in them, along with page numbers (similar to our prior indices) to the locations of those words or terms within the documents.
When a user performs a search query, Spotify's system uses the inverted index to quickly identify which tracks contain the search terms in their metadata. Often, inverted indices also employ techniques like query expansion and ranking to improve the accuracy and relevance of the search results. Query expansion involves adding synonyms and related terms to the user's original query to increase the chances of finding relevant results. Ranking involves assigning scores to each search result based on how well it matches the user's query and other factors like the popularity of the track and the user's listening history.


In our Songs database, let’s say we have hundreds of songs, and among them, there are 3 songs with ‘crazy’ in the titles. 

An inverted index, in the context of the Songs database, is a dictionary-like structure. All the terms (e.g., crazy) are associated with the list of songs that contain the term in their titles. 

In this example, we create an inverted index with a single field called "content". We add three song titles as documents to the index.

The code then searches the index for documents containing the words "crazy", "aerosmith", and "crazy love", using a QueryParser object to parse the queries. 

Notice that we find 3 documents with ‘Crazy’, 1 document with ‘Aerosmith’, and 2 results with ‘crazy’ and ‘love’ in the document.

Case Study 9.1 
How BigQuery scaled to trillions of rows at Google?
Goal: Learn why column stores are preferred for big-scale analytics

Google’s BigQuery is a fully managed, cloud-native data warehouse offered by Google Cloud that enables super-fast SQL queries using the processing power of Google's infrastructure. It allows users to analyze large and complex datasets using standard SQL, without the need for a separate infrastructure or management. BigQuery is a powerful tool that can handle petabyte-scale datasets with super-fast query performance, and it is also cost-effective. 
In 2005, Andrey Gubarev, a super-star engineer at Google, was annoyed. He wanted to analyze a web dataset to gain insights into web page trends and patterns, and he found Google’s (state of the art) infrastructure super-slow. His query was taking hours, and he wanted much faster queries (he wanted to spend less time babysitting queries for his work, so he could play foosball)! He dug into why, and how to fix this problem. He didn’t imagine his project scaling to trillions of rows at Google, becoming the core of BigQuery, and winning multiple industry and research awards, for its high impact on research and industry. (While radically improving his foosball skills.) 
Google stored billions of web documents with its associated information such as web page URL, title, body, date, and keywords. With a row-based storage approach, all data for a particular web page was stored together in one row, with each column representing a different attribute of the web page (e.g., URL, title, body, date, and keywords). When querying this data to analyze web page trends and patterns, a row-based storage approach requires reading and processing all data for each row, even if only a subset of the columns are needed for the query. For example, when analyzing web page trends by date, you would need to read and process all data for each web page (Megabytes for the HTML body), even though only the date and keywords columns (few bytes, i.e., one thousand-th the data) are needed for the query. This made querying a slow and expensive process when dealing with tens of billions of web pages.
With a columnar storage approach, all data for the web page URL column would be stored together, all data for the date column would be stored together, and so on. This allows for more efficient compression of each column (e.g., run-length encoding, dictionary encoding and bit-packing) and also allows the query to only read and process the relevant columns (e.g., date and keywords) when analyzing web page trends and patterns by date. This can greatly improve query performance and make it much faster and more efficient to analyze large datasets. 
Compression with Delta encoding
Suppose we have a column of timestamps, with 10,000 rows, each represented as a 64-bit integer. Without compression, this column would require 80,000 bytes (8 bytes per timestamp * 10,000 timestamps). However, we can use compression to reduce the storage requirements of this dataset.
One way to compress timestamps is to use delta encoding. Instead of storing the full 64-bit value for each timestamp, we can store the difference between consecutive timestamps as a smaller integer. For example, if our timestamps are sorted in ascending order, we can store the first timestamp as-is, and then store the difference between each subsequent timestamp and the previous one.
Let's say our timestamps are spaced one minute apart, starting at midnight on January 1, 2022. The first timestamp would be represented as the integer value 1640995200 (corresponding to the Unix timestamp for midnight on January 1, 2022). The second timestamp would be represented as the integer value 60 (the difference between the second minute of January 1 and the first minute). The third timestamp would be represented as the integer value 60 (the difference between the third minute of January 1 and the second minute), and so on.
Using delta encoding, we can represent this dataset using only 10,000 bytes (1 byte per minute * 10,000 minutes). This is a significant reduction in storage requirements compared to the uncompressed column, and demonstrates the effectiveness of compression techniques for reducing the storage requirements of timestamp data. Of course, the actual compression ratio will depend on the characteristics of the timestamp data, such as the time interval between timestamps and the variance in the differences between adjacent timestamps. However, this example demonstrates the intuition behind how delta encoding can reduce the amount of memory required to store sequential timestamp data.
When each column is stored in a page, with compression, we’d need much fewer pages. For queries that need that column, we’d need smaller indices and fewer IO reads. 
It's important to note that columnar storage is better suited for analytical queries, while row-based storage is better suited for transactional queries, which are often based on primary keys and require a small number of rows to be selected, updated or deleted.


Apache hosts open-source versions of columnar formats, with different forms of compression. Here’s some sample columnar code. 

Apache’s Arrow is an in-memory columnar data format that allows for efficient data processing and serialization/deserialization. Arrow has APIs in multiple programming languages, making it easy to work with data across different systems and platforms.

Parquet, on the other hand, is one example columnar storage file format that is optimized to work on disks.


Case Study 9.2
How to track user’s Spotify activity with high speed LSM trees in systems like BigTable and Cassandra? 

Goal: Design hybrid data structures for special classes of incremental updates   

Let's consider the problem of tracking user's play counts and likes for each song in Spotify. This is a high-update-volume problem, as there are millions of users who are constantly engaging with Spotify and rating different songs. In this case study, we will focus on how to update storage and indexing when we have a high volume of updates. In Section 4, we will revisit how to update these when we have multiple users buying concert tickets at the same time (without double selling the same tickets to different fans).   
Conceptually, we are tracking a key-value pair: (a) Key: a composite key consisting of user_id and song_id, and (b) Value: the activity performed (such as 'played_song', 'paused_song', 'liked_song', etc.). (In Section 4, we will revisit how to handle parallel updates in lock-based transactions.)
BigTable from Google and Apache Cassandra (originally developed at Facebook), are popular key-value databases designed for such high read and write throughput applications. We will discuss them later when we discuss distributed systems. Here, we will focus on some hybrid data structures they use for storage and indexing, for high volume read and write performance.


Definitions
Batch (or Offline) Processing: Process, store, and index data in large batches at scheduled intervals. Batch processing focuses on optimizing data layout and indexing for analytical purposes and reporting rather than real-time updates.
Motivation: Spotify may want to analyze macro user trends every month. When we have knowledge of all the data, it’s easier to store and index the data for analytical queries efficiently. E.g., sort or hash the data. 
Online Processing: Process, store, and index data incrementally as the data changes.
Motivation: A user’s set of likes and ratings may change dynamically, and Spotify’s data system needs to reflect those changes quickly. 
Hybrid Processing: Handle both analytical queries and updates to data, with more sophisticated data structures.


Intuition behind LSM trees
Log-Structured Merge-Tree (LSM tree), is a hybrid data structure for providing indexed access to files with high insert volume, such as user activity. It was designed to handle random writes efficiently, which is a weak point for many traditional data structures like B+trees.
An LSM tree combines three ideas we learnt in the past few sections: (a) buffer random write operations and organize them into multi-page disk writes, (b) keep underlying data stored in sorted order of keys, and (c) build an index over the sorted data.
First, we define Sorted String Tables (SSTables). The properties of SSTables are as follows:
Sorted: The key-value pairs are sorted by the key. This allows for efficient range queries. Earlier, we saw integer keys. Here, we use string keys (below techniques will also work  for integer keys). 
Immutable: Once written, SSTables are never modified. They can be deleted or compacted with other SSTables, but individual entries are never changed. This property greatly simplifies caching, replication, and other system properties.
Persistence: SSTables are stored on disk, and are a special type of DbFile.


Example SSTable (sst.0) 
DbFile with 6 pages and 10 rows per page, all sorted by string (lexicographic) order
Hash Index (sst.0.idx) on sorted data in DbFile

Here is a simplified view of how LSM trees works:
Write operations: Data is written to a memory buffer (called a MemTable), as well as to a commit log for durability (so the data in RAM isn’t lost if machine crashes). Both operations are fast, because MemTable is in RAM, and the commit log is a multi-page write to an IOdevice. When the MemTable reaches a certain size, it's written to disk in sorted order as an SSTable. The process is known as "flushing." Each SSTable includes an index for fast lookups. 
Read operations: When a read comes in, the system first checks the MemTable, then the most recent SSTable, and so forth, until the key(s) in each of the tables are found, or the key does not exist.
Merge operation: Over time, there will be multiple SSTables. To avoid searching through each SSTable for a key, the SSTables are periodically merged in the background. During the merge, data is read sequentially from each SSTable and written to a new SSTable. In addition, periodically, to deal with the problem of stale data (overwritten or deleted data), compaction is performed. It discards old or deleted data during the merge process to free up storage space and improve overall performance. 
Example LSM trees (basic)


Example LSM tree with 1 SSTable (sst.0)



When we inserts more data (e.g., 50 more rows) into an MemTable with space to store 10 rows 
Every batch of 10 rows will be stored in MemTable. 
When MemTable fills up, create a new SSTable (e.g., tmp-sst.1) with the data from the MemTable. And so on for the next batch of 10, till we create more SSTables (tmp-sst.1 through tmp=sst.5) in sequence, from MemTable
When a user query comes in, the LSMtree will look up sst-0 plus these additional tmp-sst tables to find the latest values.

Periodically all SSTables are merged.
That is, sst.0 will be merged with tmp-sst.1, …, tmp-ss.5.
Sst.0 will now have 11 pages with 10 rows each. And tmp-ssts are deleted.
Construct new hash (or B+tree) index

Example LSM trees for counters
Let’s say we want to increment the num_likes for a song, with song key = ‘aba’. 
Initial State: num_likes for ‘aba’ is 573. The ‘full’ SStable (sst.0) will have an entry {key = ‘aba’, num_likes=573}. That is, <key: value> is <song_id: num_likes>
The song goes viral, and we have a new stream of updates for that song.
MemTable (Partial increments) 
MemTable maintains recent partial increments 
{key = ‘aba’, partial_num_likes = 1} for each increment.
‘Fresh’ SStables (Periodic Flush): Flush MemTable changes to a set of fresh SStables.
Merging Process (Combining Counts)
Periodically, merge the full SStable and the fresh SStables and merge the values by adding the values for key =’aba’. 
Result: num_likes[‘aba’] = 573 + sum(partial_num_likes) from the fresh SStables. 
The full SStable now has the full counts, and then we delete the fresh SStables. 
Querying ‘num_likes’ for ‘aba’: Add partial counts from MemTable and full, fresh SSTables.

Policy questions:
How often should you merge? Depends on the application. The systems designer can choose when and how to merge based on time (e.g.  every hour or day), or based on size (e.g., when the temp SStables grows to “` GB” or “10 GB”), or based on traffic load (e.g., not doing as many queries now, but we expect a bunch of queries in the AM, so let’s merge a bunch of files between 2-3 AM). It’s a bit like garbage collection in Java – the system has some defaults but the systems designer gets some flexibility in choosing policies.
 


Summary of Section 2
Concepts: Hash partitioning, Indexes (Basic, Sorted, B+ tree, Text, Locality Sensitive), Columnar vs Row-based storage

Colab: NanoDB – Simple toy database to learn about storage (~100 lines), indexing and join algorithms (~300 lines). Hashing examples for text, and high dimensional data
Learning Goals
How to store data and model costs in RAM and disks? (Case Study 6)
How does NanoDB support IoDevices, DbFiles and IndexFiles? (Case Study 7)
How do OpenAI, Spotify, UberEats search over complex data fast? How to build fast indices on complex data types and high-dimensional data? (Case Study 8, 8.1, 8.2) 	
When to use columnar stores versus row stores? (Case Study 9.1 on BigQuery)
When to use hybrid structures for high volume writes? (Case Study 9.2 on BigTable and Cassandra)
Exercises PSET #1


Takeaways and Tips
Big data does not fit in RAM. Understand the physical storage layout of your data and how it affects IO performance and query speed. We need IO aware techniques to page data from slower IO devices to and from RAM.
Partitioning and indexing techniques can significantly improve search performance by reducing the amount of data that needs to be scanned for each query. Minimize the number of IO operations by selecting the best data structures for indexing and storing data. For example, using a B+tree index can help minimize the number of IO operations by reducing the number of pages that need to be accessed to locate the desired data. 
Consider using a columnar data layout when working with large datasets, especially for analytical workloads. Columnar data layouts can improve query performance by reducing the amount of data that needs to be read from disk and by allowing for more efficient compression techniques. For transactional workloads, a row-based data layout may be more appropriate, for quick access and frequent updates to individual rows. In practice, databases often store “popular” data in both row and columnar formats to support different workloads. 




3. Query Optimization 

Concepts:  Index-based lookups, Optimizing JOINs
Learning Goals
How to evaluate JOIN algorithms (Case Study 10.1 and 10.2) 
How to speed up JOINs? (Case Study 10.3 on Spanner and Spark optimizer)

Exercises 
Pset #1 and NanoDb Colab

Case Study 10
How could Spotify optimize basic queries? 
Goal: Learn how to optimize queries to make them run faster and cheaper


For example, when a user wants to refresh their playlists, and explore their most listened to songs, the app will be slow and inefficient if we had to scan the rows for 300 million users to find the relevant data. 

When an index exists on the user_id column, the database can use it to quickly locate the rows that match the WHERE clause condition, user_id = 123. This speeds up the execution time of the query by reducing the amount of data that the database has to scan.
In the GROUP BY clause, the database groups the rows based on the song_id column. Even with an index, the database still needs to hash-partition (or sort) the rows to group the ones with the same song_id together. However, the number of unique song_ids is likely much smaller than the total number of rows. 
Finally, in the ORDER BY clause, the database sorts the result set by the number of listens in descending order. This operation can be expensive, especially if the result set is large.
That’s for one query, and for one user. In general, millions of users are active on Spotify at the same time, performing a variety of actions (executed behind the scenes using SQL). The DB’s query optimizer is responsible for executing all these queries fast for a good user experience.  The query optimizer analyzes each query and the available indexes, statistics, and other information about the data, and then generates a query execution plan that it believes will be the most efficient way to execute the query. This includes selecting the most appropriate indexes to use, reordering operations in the query, and making other adjustments to the query to improve its performance.


Let’s review our Recommendations query.

Here's how the query optimizer might break down the steps for the given query:
JOIN: The query optimizer will first join the Listens table with itself to find all pairs of songs that are listened to by the same user. The optimizer will evaluate the costs of different JOIN algorithms (next case study) based on the size of the data and the presence of indexes.
GROUP BY: After the join, the query optimizer will then group the pairs of songs by the two songs' IDs and count the number of common users for each group. Once again, it will evaluate the cost among GROUP BY algorithms. (e.g. SortBy, HashBy) 
FILTERING: Finally, the query optimizer will filter the groups to only include those with more than 10000 common users.

In the next Section, we’ll discuss algorithms to execute each of the above steps, and also to evaluate the cost of each execution.


Case Study 10.1
How NanoDB optimizes JOINs? 

Goal: Learn how to optimize JOIN queries


Preview of algorithms
Joins two (or more) tables on IO devices as follows

BNLJ (Block Nested Loop Join): Iterates over all pairs of table blocks.
HPJ (Hash-based Partition Join): Partitions each table using a hash function, then joins each corresponding partition.
SMJ (Sort-Merge Join): Sorts each table first. Then merges them by traversing pages in sorted order.

Intuition: Exploit memory efficiently by reducing the amount of data that needs to be compared during the join process.



In this Section, we’ll discuss algorithms and the costs to execute JOINs.  
Concept: Basic Joins


BNLJ is a block-nested loop algorithm used to join two tables R and S. 

In the first step, the pages of table R are read into RAM, B pages at a time, and cached in memory. In the second step, the pages of table S are read, and the join operation is performed with the cached pages of table R, to produce R-join-S.

BNLJ executes a join with its nested-loops in Steps 1 and 2 on every pair of pages (also known as blocks). Hence it’s called Block-Nested Loop Join, or BNLJ for short.




Consider a JOIN on song ID for the Songs and Listens tables to produce Songs-join-Listens table. For example, consider row (14, ‘nc’, ‘..’) in Songs, and rows (14, ‘eq’, ‘..’), (14, ‘xo’, ‘..’) in Listens. When we match these rows during the JOIN, we see (14, ‘nc’, ‘..’, ‘eq’, ‘…’) and (14, ‘nc’, ‘...’, ‘xo’, ‘...’) as part of the final output. 

In this example, Songs-join-listens stores up to 4 rows per page in its DbFile. As always, NanoDb uses the pageSize and the rowSize of the result while computing the number of rows per page.  



In BNLJ, notice that we had to loop through every page in Songs and Listens to execute our joins. Next we discuss how to speed up joins with Hashing and Sorting. 
Concept: Fast Joins with Hashing


In Hash-Partition-Join, 
We first Hash-Partition(R) and (S) separately, with the same hash function.
Next, we JOIN only matching partitions using BNLJ. That is, we join R_i and S_i to produce R_i-join-S_i. 







For example, we partition Songs and Listens into 4 partitions by hashing song ID. For example, Songs’ row (14, ‘nc’, ‘..’) is hashed into Songs.2, and Listens’ rows (14, ‘eq’, ‘..’) and (14, ‘xo’, ‘..’) are hashed into Listens.2. We can run BNLJ(Songs.2) and BNLJ(Listens.2) we’d get the matching join rows for rows that are hashed in partition #2, including rows for song ID = 14. Also, we don’t need to run BNLJ on Songs.2 versus Listens0, Listens.1 and Listens.3, because the matching values for rows in Songs.2 will only be in Listens.2 

That is, we partition our problem, and cut down on the number of pairs of pages we need to compare. 


Concept: Fast Joins with Sorting








Now let’s summarize how to do a Sort-Merge-Join (SMJ) algorithm to join two tables R and S. 

In Step 1, both tables are sorted and stored as sorted DbFiles. In Step 2, the algorithm iterates through each page of R and S in sequence, and merges the two sorted files by comparing their elements. When there is a match, the algorithm scans through all equal values and appends them to an output file. When there are duplicates, the algorithm ‘backs up’ (i.e., tracks matching duplicates to match). 
The algorithm continues until it has gone through all the pages of both R and S. 

In SMJ, we first sort Songs into Songs-2 and Listens into Listens-2 (Step 1). In Step 2, we sequentially scan the pages of Songs-2 and Listens-2 for merging.

To gain a better understanding of Step 2, we can examine the first and last pages of the Songs-2 and Listens-2 tables. For instance, let's say the first page of Songs-2 contains the row (14, ‘nc’, ‘..’), and Listens-2's first page has matching rows (14, ‘eq’, ‘..’) and (14, ‘xo’, ‘..’). Since the rows are sorted, we can conclude that no other pages can have matching rows for song ID 14.

Similarly, the 34th page of Songs-2 has rows (499, ‘dh’, ‘..’), but the highest song ID on Listens-2's 14th page is 486. Because the DbFiles are sorted, we know that song ID 499 cannot appear in any page before Listens-2's 14th page. Therefore, if there are matching tuples for this pair of rows, they can only be found on page 15 or beyond. Thus, we don't need to read pages 14 and earlier again, unlike in BNLJ's nested loops. By reading the pages of Songs-2 and Listens-2 in sorted order, we can perform our joins efficiently.

In some cases, we may need to "backup" (i.e., “go back”) and reread prior pages when tables have duplicate join match values that span pages. For instance, suppose a new release becomes extremely popular, and the Listens (sorted) table contains millions of rows for that specific song ID, spanning multiple pages. Additionally, an Advertisements (sorted) table may have millions of rows for ads shown for that song ID as well. In the worst-case scenario, we may need to read all matching pages for both the (sorted) Listens and Advertisements tables multiple times. Although the algorithm will still work, it may become as expensive as BNLJ, resulting in decreased efficiency.  

IO costs for JOINs
We now discuss IO costs for the different algorithms we’ve seen so far. We discussed [1] and [2] earlier. In [3], [4] and [5], we discuss the IO costs for different BNLJ, HPJ and SMJ algorithms, along with examples on how to use these for real tables. We compute these by (a) counting the number of pages read and written between RAM and disk, and (b) multiplying by the corresponding read (C_r) and write costs (C_w). We use OUT to indicate the number of output pages, for simplicity. We’ll later discuss how we can estimate the size of the OUTPUT, based on how many rows match. 
Intuition for IO costs 

When using BNLJ(R, S), we utilize a nested loop to iterate through the pages of R and S. We read B pages of R at a time and store them in RAM, before reading S's pages to join with R's cached pages. We factor in C_r for read costs and C_w for write costs, multiplied by the number of pages and the output size, respectively. 

It is important to note that BNLJ(R, S) and BNLJ(S, R) will produce the same results. But their IO costs will not be the same. (Just swap R and S in BNLJ’s equation, and it’s easy to see why.) Therefore, NanoDB decides which table should be in the inner loop versus the outer loop, to minimize IO costs.

HPJ(R, S) involves first performing HP(R) and HP(S), then partition-joining (PJ(R, S)) the two sets of partitions. Equation (1) reflects the total cost, whereas Equation (2) represents the cost of HP(R) and HP(S) as discussed previously. 

The cost of PJ(R, S) is harder to model because it depends on the spread of the hashing function across the partitions and the number of matching rows in the JOIN. Equation (3) provides a simple approximation assuming a well-spread hashing function. If there is a hashing skew or many duplicates, it is worth trying an alternate hash function or join algorithm.

HPJ(R, R) is a self-join. It’s similar to HPJ(R, S), except we don’t need to HP(R) the same table twice, nor read each partition twice for the JOIN.  

In the special case when C_r = C_w = 1, we can simplify the IO cost model of HPJ(R, S) to 3(P(R)+P(S)) + OUT (with basic algebra). 

SMJ(R, S) works by first sorting both R and S based on their join keys. We then sequentially scan the pages of both relations in order, comparing each pair of rows with matching keys. We factor in the cost of sorting, scanning, and writing the output, multiplied by their respective sizes, in Equations (1) to (3). 

In MergeJoin(R, S), when there are no duplicates during merging, we need to only read P(R) + P(S) pages once each in sorted order, at a cost of C_r each. However, in the worst case, all the input rows could have the same value for the join key. In such a case, all rows have to be joined, and produce a cross product.  

Also, SMJ(R, R) is a self-join. It’s similar to SMJ(R, S), except we don’t need to Sort(R) the same relation twice, nor read the sorted R twice.

Comparing IO costs 
To gain a better understanding of the tradeoffs between BNLJ, HPJ and SMJ, let's review some examples. 

We will consider a database called db100 with B=100 and C_w, C_r = 1. We will explore various scenarios with different table sizes. Examples 1 to 3 will analyze different sizes for Songs1 and Listens1, taking into account whether the tables are sorted. Example 4 will focus on self-joins, and Example 5 will model the cost for the song_similarity CTE. Additional examples can be found in the NanoDB Colab notebook, where you can experiment with different scenarios for B, C_r, C_w, and also table sizes.





We plot a graph (log scale) to visualize the IO costs for the above examples using BNLJ, BNLJ-reverse, SMJ, SMJ with duplicates (bad backup), HPJ, and HPJ with skewed data (e.g., bad hashing or numerous duplicates).

Overall, HPJ and SMJ tend to outperform BNLJ, especially for big tables. However, if there are many duplicates, BNLJ may be the more cost-effective option. SMJ-BadBackup and HPJ-BadSkew will incur additional costs due to the sorting (or hashing) pre-processing step. In our simplified description we do not account for more sophisticated page caching strategies that are typically used in practice for SMJ and HPJ, similar to those employed by BNLJ. Although these ideas are separate, they are often combined in practice to optimize. 


Case Study 10.2 
Query Optimizers in Spanner and Spark

Goal: Learn how popular query optimizers work

Google Spanner's query optimizer is a critical component of its fully managed, distributed relational database system. Here's a technical overview of how the Spanner query optimizer works.  [Good examples in Spanner’s deep dive].
Relational Algebra Representation: When Spanner receives a SQL query, it parses it into an internal representation based on relational algebra. This representation forms a tree structure where each node represents an operation of the original SQL query. For example, table accesses are represented as leaf nodes, and joins are represented as binary nodes with the two relations to be joined as inputs.
Heuristic Optimization: In this stage, predefined rules or heuristics are applied to improve the query plan using logical improvements. Examples of heuristic optimizations include: (a) applying WHERE conditions on the relevant table as early as possible (e.g., pre-joins), (b) converting outer joins to inner joins where possible.
Cost-Based Optimization: In this phase, Spanner uses a cost-based optimization using estimates of IO costs to choose the best available alternatives. It involves evaluating different execution plans and selecting the one with the lowest expected cost, where cost is based on factors like data distribution, available indexes, and network latency.
Apache Spark’s SQL adopts a similar approach for speeding up SQL queries.
Example for evaluating costs of query plans

Consider the above example query to compute highly recommended songs. (We use this artificial query to help explain a few concepts for cost-based optimizations. We could have written the logic using a simpler query.) Spanner’s query optimizer will evaluate a variety of plans, including the below two query plans. 

Query Plan #1: Using SMJ

For simplicity, we assume we explicitly output partial results into tables JRL, JRLG, etc. below. In practice, we can do better (by reusing partial outputs), as we’ll see later in Tips.
Goal: Join Recommendations and Listens based on song_id, user_id. How? 
Use SMJ(Recommendations, Listens) on sort key = [song_id, user_id]
Store output in table `JRL’ with schema = [user_id, song_id, recommendation_id].
Cost = BigSort(Recommendations) + BigSort(Listens) + MergeJoin(Recommendations, Listens) + C_w*P(JRL)
Goal: GROUP BY song_id on JRL to count recommendations. How? 
Scan table JRL (sorted by [song_id, user_id]). Count per-song_id recommendations. For example, consider the following sorted table (JRL) with song_id, user_id, recommendation_id rows = [...., (497, 584, 1), (497, 1024, 4), (497, 2014, 3), (500, 584, 1), (500, 1024, 4), …]. We see that all the song_id=497 rows are in order, and it’s easy to compute an aggregate over rows with song_id=497 with a single counter in RAM, while scanning the table.   
Store output into table JRLG with schema = [song_id, counter].  
Cost = C_r*P(JRL) +C_w*P(JRLG)
Goal: ORDER BY count(recommendations). How? 
BigSort(JRLG) by recommendations count. 
Store output in table JRLGO with schema = [song_id, recommendation_count]
Cost = BigSort(JRLG).


Query Plan #2: Using HPJ

Goal: Join Recommendations and Listens. How? 
Use HPJ(Recommendations, Listens) on hash key = [song_id, user_id]
Store output in table JRL with schema = [user_id, song_id, recommendation_id].
Cost = HP(Recommendations) + HP(Listens) + PartitionJoin(Recommendations, Listens) + C_w*P(JRL)
Goal: Group by song_id on JRL. How? 
HP by song_id and store in JRLH. Notice we are hashing by song_id in this step, because our JRL was partitioned by [song_id, user_id] to make join easier.
Then scan JRLH, and count per-song_id recommendations with a counter. For example, consider the following partitioned table (JRLH) with song_id, recommendation_id [.... (497, 584, 1), (497, 1024, 4), (497, 2014, 3), (200, 584, 1), (200, 1024, 4), …]. We see that all the song_id=497 rows are in the same partition. With a small number of counters for song_ids in that partition, we can compute an aggregate over rows with song_id=497.
Store output into table JRLG with schema = [song_id, counter].  
Cost = HP(JRL) + C_r*P(JRLH) + C_w*P(JRLG)
Goal: ORDER BY count(recommendations). How? 
Use BigSort(JRLG) on count(recommendations). 
Store output in table JRLGO with schema = [song_id, recommendation_count]
Cost = BigSort(JRLG)

Tips for how to pick amongst query plans
We saw two example query plans. In practice, the query optimizer uses the following techniques to generate many (10s to 100s) such viable query plans to execute a specific query). Then it evaluates each of their IO costs, before picking the cheapest option. The ``generate and evaluate viable plans’’ phase is much cheaper versus executing a specific query plan, which involves IO costs. It’s akin to using a GPS (seconds) to evaluate all viable traffic routes from Stanford to San Francisco, picking the best route, and then taking the hour to complete the actual drive.
1. Which columns to Sort or Hash By: When deciding which columns to sort or hash by, consider the following:
Join Conditions: Columns involved in join conditions are prime candidates for sorting or hashing. For example, if you're joining on user_id and song_id, consider sorting or hashing by one or more of these columns.
Grouping Criteria: If your query involves grouping, sort or hash by the columns you're grouping by. For instance, if you're grouping by song_id, sort or hash by song_id.
Aggregation Fields: If you're aggregating data (e.g., counting recommendations by song_id), ensure that the columns needed for aggregation are sorted or hashed appropriately. For example, when you scan a table sorted by song_id, you know all the song_ids will be in order. With a simple counter (in RAM), you can SUM or COUNT an affiliated column during the scan. For example, consider the following sorted table with (song_id, recommendation_id) rows = [.... (497, 1), (497, 4), (497, 3), (500, 1), (500, 4), …]. We see that all the song_id=497 rows are in order, and it’s easy to compute an aggregate over rows with song_id=497 by scanning the sorted table.   
2. Reusing Work Across Steps: Reusing work from one step to another can significantly optimize query processing. Here's how:
Sort-Merge Join (SMJ):
If you've performed a Sort-Merge Join (SMJ) using a specific sort order (e.g., song_id), and the next step requires data in the same order (e.g., ordering by song_id), you can reuse the sorted data from the join in the subsequent step. There's no need to sort it again, saving computational resources.
In SMJ, if you've already sorted or merged data during the join step, take advantage of that sorted order in grouping or aggregation steps.
When planning subsequent steps, consider how to leverage the ordered data efficiently.
Hash Partition Join (HPJ):
Unlike SMJ, HPJ doesn't inherently produce ordered data. If you need ordered data in a later step, you may need to perform an additional sort operation.
However, you can reuse the partitioned data efficiently. For example, if you've hashed data by song_id during the join, and the next step involves grouping by song_id, you can use the pre-partitioned data for grouping without recomputing the hash.
When using HPJ, focus on optimizing the partitioning step, as this operation can be resource-intensive. Ensure that the partition keys align with the subsequent grouping or aggregation criteria.
3. Efficiency Considerations: Consider the trade-offs between sorting and hashing:
Sorting is beneficial when you need data in a specific order for multiple steps, as you can reuse the sorted data efficiently.
Hashing is more suitable for scenarios where you need to partition data based on multiple criteria (e.g., user_id and song_id) and then perform operations on those partitions.
Hashing can lead to a more even distribution of data across partitions, which can be advantageous for parallel processing. On the flip side, if there’s a hash skew (e.g., data has lots of duplicates, or if we picked a poor hash function), HPJs could have poor ‘worst-case’ performance.
Always aim to minimize unnecessary work. If a subsequent step requires data in a specific order, try to design the preceding steps to produce that order efficiently, whether through sorting or hashing.
4. Profile Query Execution: Profiling the execution of your query can help identify areas where work can be reused or optimized. Use database profiling tools to gain insights. 
By carefully selecting columns for sorting or hashing and reusing work efficiently, you can streamline the execution of complex join queries and improve overall query performance.
Advanced Query Optimization
In addition to the BigSort and HashPartition based techniques, modern query optimizers consider
Index Structures for WHERE and ON conditions. Optimizers also evaluate using (or building) index structures (B+trees, LSM trees, etc) when columns are filtered. Databases also keep statistics on data skew and ‘shape’ for columns to help pick hashing versus sorting versus indexing filters.   
Detailed modeling of IO costs: We use a simple per-page access + throughput cost model. Optimizers often build IO models of sequential layout of pages (e.g., on a hard disk platter), IO contention, and even performance under different temperatures.
Distributed query processing. Optimizers model network latency, data distribution, load balancing, and how to reduce network data movement.     


Case Study 10.3 
Evolving a Spotify-like app with new features

Goal: Learn how data systems are designed for different goals by combining our different Lego blocks

Modern data systems adopt a modular architecture, much like Lego pieces. We can combine each piece into a ``system of systems’’ to form a richer structure, and to address specific use cases in an optimized manner. For example, we saw how to build a basic Spotify App with a SQL (or variant) engine for managing structured data related to Songs, Users, and Listens, and storing media files in a key-value store. Let’s explore a few directions in which such an app could evolve, based on user and product needs. 
Let’s say your team picks the following goals for your road map. Here’s how you could start breaking down the goals and put together the right pieces of a full system.

Figure: “System of Systems” to solve for different goals

Goal 1: Artist-Facing UI for Royalty Stats and Trend Analysis
Problem: How to quickly introduce and experiment with new product experiences.  Technical Idea:
Use the SQL engine to run data aggregation queries to count the number of listens per song over the past month and analyze geographical trends via basic zip code mapping. For example, compute aggregation statistics from the 2000 fanFaciliats for Beatles’ Yesterday in zip=94022.
Artists want to find trends with a custom date range UI (e.g, influence after a song release). Create a B+ tree index on (say) Listens.<song_id, date> using your DB’s CREATE INDEX tool for date range queries. 
Goal 2: Helping Artists Understand Their Fan Preferences
Problem: How to uncover the latent preferences and characteristics of fans and songs, and to find clusters of similar users or songs for targeted marketing initiatives. Technical Idea:
Engineered features or Embeddings + LSH: Generate embeddings for users and song features (e.g., lyrics or social-media fan posts, or song-level tempo, timbre). Utilize LSH indices to speed up similarity searches, personalized recommendations.
Goal 3: Facilitate Local Fan Club Meetups
Problem: How to identify hyper-local communities, when zip codes don’t provide the needed resolution for meetups. Technical Idea:
Use H3 Geo Hashing to map a user’s address to H3 cells. Find high-density areas for local fan club meetups based on user geographic data, target zones with > 100 fans for meetup and listen parties. (e.g., GROUP BY H3(address), HAVING count(user) > 100). Most DB engines support geo indexing tools as extensions (e.g., H3 or Postgres’ PostGIS).  
Goal 4: Track the number of fans at Listen parties simultaneously listening to songs ‘Live’
Problem: How to scale up the number of updates, as fans tune in and out on their app. Technical Idea:
Count the number of fans listening to a song `live,’ e.g., 50,000 users tuning into Taylor’s latest song drop. Many DB engines will use LSM Trees (automatically or with a configuration change) to manage such high-frequency data writes, ensuring system responsiveness and accuracy. Roughly, for these writes, the DB will keep partial live_listen_counts in MemTable, flush into partial SSTables (say) every 5 mins, and merge into full SSTables every hour for later analysis.  
Explore local trend changes at Listen parties. Explore combining LSH indexes with LSM’s flushing and merging LSH trees (as opposed to SSTables). (While I personally don’t know anyone who has done this, it’s a viable technical idea to extend LSM’s merges and flushes for LSH indexes. I expect there’s also likely a better product idea than the fake one I’m making up to illustrate a point on how LSM ideas could work with different indices). 
Goal 5: Anticipate a significant surge in user traffic when a new song premieres post-marketing event
Problem: How to scale user traffic across the board. Technical Idea:
Evaluate Hash Partitioning the data based on songIDs, userIDs (or other columns) to distribute table partitions across a cluster of machines, to balance load on reads and writes and use parallelism for scale.
Goal 6: Expose a SQL API to interface with a Concert Manager App for personalized local concert recommendations
Problem: For business needs, you’ve been asked to offer a rich API, while preserving user privacy on aggregates. You want to pre-design for a future “app store” use case, where multiple third-party apps can access this data. Technical idea:
Use SQL with integrated differential privacy noise (either built-in like in BigQuery or Spanner, or as an extension package) to protect user data, while releasing the aggregates needed. Setup per-app privacy configurations to handle different tiers 
To provide a high-level interface, consider adding another layer on top of the SQL API, inside web-friendly RESTful endpoints. For example, an endpoint like /concerts/recommendations could trigger a SQL query based on user preferences and location.  Implement robust authentication and authorization mechanisms to ensure only the right apps can access the data, reinforcing data privacy and security. For super-power apps or when you’re designing the right APIs, you may also add a /concerts/sqlapi with more direct access to the test database for you to rapidly test ideas. 

Goal 7: ETL Processing of Incoming Feeds Data from Third-party Data Providers
Problem: Ensure accurate and efficient Extraction, Transformation, and Loading (ETL) of incoming feeds data while maintaining data quality and enabling data reconciliation and versioning. Most data apps rely on some external data (e.g., song lyrics or album cover data) to enhance the user experience, and most feeds are messy. Technical Idea:
Extraction:
Set up automated processes to extract incoming feeds data at scheduled intervals or in real-time as the data becomes available.
Implement checks to verify the integrity and completeness of the extracted data, ensuring it meets any predefined quality standards.
Transformation:
Design transformation pipelines to clean, normalize, and enrich the extracted data.
Incorporate data quality checks within the transformation process to identify and rectify any inconsistencies, duplicates, or missing values in the data.
Provide mechanisms for data reconciliation to ensure that the transformed data accurately represents the original data source, allowing for traceability and auditability.
Loading:
Create versioned tables to store the transformed data, allowing for tracking changes over time and maintaining a history of data alterations.
Utilize a versioning system to label different versions of the data, enabling easy rollback, comparison, and analysis of data changes.
Load the transformed data into the versioned tables in the database, ensuring that each version is accurately recorded and easily retrievable.
Implement a reconciliation process post-loading to verify that the data has been loaded correctly and completely into the destination tables.
Monitoring and Alerting:
Develop a monitoring and alerting system to track the ETL process, providing real-time insights into the process performance, data quality issues, and any errors in the pipeline.
Configure alerts to notify the appropriate personnel in case of data quality issues or failures in the ETL process, ensuring timely resolution of any problems.
Implement detailed logging within the ETL process to capture events, errors, and data transformations, aiding in troubleshooting, and performance optimization. Document the ETL processes, data quality checks, and reconciliation procedures to ensure transparency and ease of maintenance.
This goal sets a strong foundation for handling incoming feeds data efficiently and accurately, ensuring that the data loaded into the system is of high quality, reconciled, and versioned, facilitating a reliable and traceable data loading process.

Takeaway: We can combine our discrete ideas from Sections 2 and 3 (e.g., BigSort, HashPartitioning, Indexing, JOINs, and query optimizers) to solve for specific use cases. 


4. Parallel Transactions

Learning Goals
How to build apps with transactions? (Case Study 11 and 12 on Taylor Swift’s ticket sales)
How to build a basic transactional system? 
How to prove correctness of concurrent transactions? 
How to build high speed read-write LSM trees in systems like BigTable and Cassandra? (Case Study 12.2 How to track user’s Spotify activity)
What are good data structures for concurrency in semi-structured data? (Case Study 12.3 on Google Docs’ real-time collaboration)

Colab: Concert Transactions – Learn how developers use transactions (~100 lines), build Transaction systems with Locks/Logs (~300 lines), and concurrency theory (~200 lines). Exercises:  Homework3 

Case Study 11
Taylor Swift and the Ticketmaster disaster

Goal: Learn how to apply SQL to build transaction applications. 

Taylor Swift announces "The 2023 Eras Tour" and her fans go absolutely wild! It's like trying to get the last slice of pizza at a party - everyone wants a piece of the action. The demand for tickets is so high that it crashes Ticketmaster's website multiple times, leaving fans frustrated and disappointed. Some Swifties even had to endure a two-hour wait just for a chance to grab tickets! Taylor Swift, on Instagram: "I'm so sorry for the frustration and inconvenience this has caused."
With 52 show dates and 3.5 million fans pre-registered for the Verified Fan Presale, about 1.5 million fans received invite codes and this massive wave of excitement led to over 2 million tickets being sold in a single day. The website got hit with a colossal 3.5 billion total system requests, which was four times its previous record!
When you're trying to snag tickets for a concert like Taylor Swift's "The Eras Tour," you're participating in a transaction. This ticket buying adventure is a virtual handshake where you exchange something valuable (in this case, money) for something else valuable (those sweet concert tickets), with some inbuilt guarantees. 
Transactions in a Ticketmaster-like app
Let’s start with a simple example of how concurrent transactions work on a non-peak day. 
Example: Concert Tickets (Buy and Refund)
Alice is trying to buy concert tickets. For Alice’s purchase, we need to 
Check if there are enough tickets in the inventory, 
Verify if Alice’s credit card authorizes the purchase, and 
Confirm the sale to Alice, execute the credit card purchase, and update the inventory
All three steps need to happen. We can’t confirm the sale to Alice if her credit card declines or if there aren’t enough tickets. Similarly, we can’t sell Alice’s tickets to another fan who’s trying to buy tickets at the same time. Similarly, for a refund ticket request, we’d execute a refund to Alice’s credit card and update the ticket inventory.    


Definitions
Transactions guarantee a few key properties, collectively termed ACID, in this situation:
Atomicity: Alice finds two tickets for the concert and proceeds to checkout. During the payment process, her credit card is declined. In this case, the entire transaction should be rolled back. This means the two tickets are not issued to Alice, her payment isn't processed, and the ticket inventory is not reduced. Atomicity ensures that either the entire transaction occurs or none of it does, leaving the system in a consistent state.
Consistency: Bob successfully purchases a ticket for the concert. The system must maintain consistency by updating the ticket inventory, recording Bob's user data, and reflecting the transaction in the financial records. If the database were inconsistent, it could lead to errors like overselling tickets or incorrect financial data. By ensuring consistency, the system remains reliable and accurate for all users.
Isolation: Alice and Bob are trying to buy the last available ticket for the concert at the same time. To maintain isolation, the system “locks” the ticket when either Alice or Bob selects it, preventing the other from purchasing it simultaneously. Once the transaction is complete for one of them, the lock is released, and the remaining inventory is updated accordingly. Isolation ensures that each transaction is independent of others, preventing double-selling of tickets.
Durability: Bob successfully buys a ticket, and the transaction is completed. The system must permanently record this transaction, ensuring that Bob's ticket information is securely stored and available to him, even in the event of system failures or crashes. Durability guarantees that once a transaction is complete, the changes made by the transaction persist, providing users with confidence in the system's reliability.


Buckle up for some transaction action! 
Example Concert tickets app – SQL with Transactions for purchases and refunds


For this example, we’ll use a Concerts table to maintain the number of available tickets in each concert. 

We will manage multiple concurrent users who are simultaneously purchasing tickets and requesting refunds, through a web/mobile app. This scenario ensures that the system can efficiently handle multiple users interacting with the application at the same time, without compromising the integrity of the ticketing process. You can play with the below code in the Concerts Transactions Colab.

We use two functions to handle ticket purchase and refund processes for a set of concerts. We use SQL transactions to ensure ACID. We use conn, for our connection to the database. (Focus on the SQL part, and less on python.)

Transaction for purchase_ticket :
We start a new transaction using the BEGIN statement.
We get the number of available tickets for the required concert, using a SELECT statement.
If there are no available tickets, the transaction ends without making any changes.
If tickets are available, we simulate a user’s payment (with a 50% chance of failure due to insufficient funds). If the payment is successful, the number of available tickets for the concert is reduced by 1 using an UPDATE statement.
If the payment fails, the function prints a message, and the transaction is committed without updating the number of available tickets.
Finally, the transaction is committed using conn.commit().

Transaction for refund_ticket:
We start a new transaction using the BEGIN statement.
The transaction increments the number of available tickets for the specified concert_id by 1, with an UPDATE.
Finally, the transaction is committed using conn.commit().


As we see in the above example, SQL makes it easy to write transactions with BEGIN/COMMIT blocks, ensuring data consistency and simplifying complex and concurrent operations in applications. Transactions are designed to follow the ACID properties (Atomicity, Consistency, Isolation, and Durability), which guarantees that operations are executed in a reliable and robust manner. 
With the use of SQL transactions, developers can focus on implementing their application’s business logic without worrying about the potential issues caused by concurrent operations, ultimately improving the application's performance and reliability. You can review more examples in the Concerts Transactions Colab. 
In the next 2 case studies, we’ll dive deeper into how to build such a transactional backend, and how to make it easy for application developers to use.

Concepts 11.1
How to build NanoDB’s transactions?
Goal: Preview building blocks of a basic transaction system to manage concurrent (or parallel) access to shared resources like concert tickets availability

In our Concerts example, multiple users are trying to purchase or refund tickets for the same concert simultaneously. This can lead to problems, such as selling more tickets than available or incorrect ticket counts after refunds, or lost tickets and double bookings if the system crashes. We saw how to avoid these problems using BEGIN/COMMIT/ABORT blocks in SQL transactions.
In this section, we’ll dig into how NanoDB implements such transactions for ACID properties. Here’s a roadmap of what’s coming up next. We’ll put all these back together in Section 12 with some simplified code for NanoDB’s transactions.
Deconstruct Transactions: Break down concurrent transactions into Read/Write actions.
Optimize by Reordering: Reorder Read/Write actions in concurrent transactions much like a compiler optimizing CPU instructions in high-level software. We’ll see examples of how we get 25x – 100x speedups by reordering actions across transactions, versus executing each transaction serially, one after the other. 
Correctness: We'll get intuition on reorderings that yield correct results.
Locking: We’ll see how locks control access to shared resources, such as the available tickets for a concert. We’ll discuss locking algorithms that give us correct reorderings and big speedups.
Logging and Recovery: Lastly, we'll dig into the mechanisms behind transaction rollbacks and durability during system crashes. Logging helps track the history of transaction events and outcomes, allowing the system to monitor and audit transactional activities, and recover from system crashes. 
Roughly, in the below figure we see 
A set of concurrent transactions (T1, T2, T3, T4). Each transaction reads and writes some values (e.g., concert tickets). We use green to visually represent reads, and red for writes. T1 may check availability (i.e., reads) for multiple concert dates or seats before selecting and purchasing a ticket (i.e, write or update seat map or inventory). 
A Transaction Manager. This manager picks the order in which the read and write actions are executed. It may choose to execute the transactions serially, one transaction after the other, or may choose to interleave the actions. The manager is responsible for overall correctness and performance, and for that it uses some subsystems (e.g,  Scheduler) and data structures (e.g., Locks and Logs) that we’ll learn about more in the rest of this Section.

Figure: Overview of how to build transactions

Reordering rules
Rule 1: DBs do not care about the order of transactions. That is, T1→ T2 → T3 and T2 → T1 → T3 or T3→ T2 → T1 are all fine. 

Why? 
Conceptually, the database does not care if Alice’s T1 or Bob’s T2 happens first. If the developer needs a specific ordering (say, T1 has to happen before T2 before T3), they can make transaction T4, with logic for T1, T2 and T3 in the desired order inside a BEGIN/COMMIT. In fact, this flexibility helps the DB reorder Transactions as needed, for big performance gains by resequencing IOs.    
  
Rule 2: DBs care about the order of Read and Write actions across the transactions. 

Why? The main intuition is that DBs focus on avoiding double-booking of tickets, and guaranteeing tickets after payment, etc. We’ll soon see more specific criteria for this rule to ensure the transactions are ACID.

Reordering Goals: 
Correctness
Transactions need Isolation (for ACID). That is, they should feel as if they are alone and are acting independently. 
The Transaction Manager (TM) guarantees transactions are isolated, and transactions don’t see partial changes from each other, for correctness. In other words, the transactions should feel like they were executed one after the other, serially, in some order. 
Execution: The TM will interleave actions, so that each transaction feels isolated, and we get performance speedups. We’ll soon see how TMs achieve these goals by following Rules 1 and 2 in specific ways.        

Why? Imagine you’re working on your project. Thirty minutes in, you are hungry. Later, you want to message your friend to clarify a question. Also, you want to buy a laptop on Amazon. Your friend may respond after some time, and Doordash may take 30 mins to deliver food, Amazon may take a day. Would you wait to finish your project, before initiating these “transactions?” 
You’d probably interrupt your project to initiate these transactions, because these will take some time externally, and you’ll hear back “asynchronously.” 
DBs (or the TM part of the DB) take a similar approach, because of IO costs. They may interrupt some CPU work for a transaction to start a read or write action that an IO device can work on in parallel. When the IO device finishes a read (and data is paged into RAM), the TM can decide when to start work on that. (Ditto with writes.) 
At the same time, your Doordash order and Amazon order may conflict, especially if you have limited funds. And your VISA card provider may pick which purchase goes through. 

Here’s an overview of the steps we’ll go through in the next ~40 pages. First, concurrency theory for correctness, and then how to use that basis for building a practical transaction manager system. Don’t focus on the details yet, we’ll work through them in the next 40 pages. Consider this as a roadmap for how the different pieces will fit together.


Concepts 11.2
Correct reorderings for concurrent transactions

Goal: For concurrent transactions, learn which action reorderings give correct results


Example: Schedules for 3 Transactions and 2 Concerts
Three transactions (T1, T2, T3) read and write A and B (available tickets for Concerts A and B). In our notation, we’ll only focus on the read and write actions, and not how the data is modified (e.g., A -=1 or A*=10). Here are some example schedules.
T1: Purchase Concert A’s ticket  – Read A, decrement A, write updated A.
T1’s schedule: [T1.R(A), T1.W(A)] 
T2: Check ticket availability for Concerts A and B. Buy a ticket for Concert B.
T2’s schedule: [T2.R(A), T2.R(B), T2.W(B)]
T3: Purchase a ticket for Concert B
T3’s schedule: [T3.R(B), T3.W(B)]
In the Concerts Transaction Colab, we can play with these schedules, and algorithms to help us test for transactional correctness.


Definitions 
Actions (or operations): Actions in a transaction involve accessing and modifying data in a database through reads and writes.

Motivation: Read and write actions are the fundamental building blocks of a transaction. In a transaction, a read action is usually followed by a write action, where the data is read, processed, and then updated in the database. E.g., [T1.R(A), T1.W(A)]. We may also have a T1.W(A) without a T1.R(A) (a “blind write”) or a set of Reads only. 
IOlag (or IO cost) is the time between the start of a read action by the CPU and the retrieval of the value from an IO device such as RAM or SSD. (Write IOlag is the time for the CPU to write to an IO device.)

Motivation: IOlag helps us model when the CPU is idling, waiting for an action to complete. We can reduce CPU idling, with work (interleaving) from other transactions. 
Serial Schedule: A sequence of actions where all actions of one transaction are completed before any actions of the next transaction begin. E.g. [T1.R(A), T1.W(A), T2.R(A), ...T3.R(B), T3.W(B)], where all T1’s actions are run before T2’s actions, and T3’s actions. 
Motivation: Serial schedules maintain consistency in the database. Each transaction is executed completely before the next transaction starts, and there is no contention on shared data between transactions. However, they can lead to poor performance since each transaction must wait for the previous one to finish.
Interleaved Schedule: A sequence of actions from multiple transactions that are executed concurrently, with their operations interleaved or mixed. E.g., [T1.R(A), T2.R(A), T1.R(B), …], where T2.R(A) starts before T1 is finished.
Motivation: Interleaving often improves performance over serial schedules, and reduces CPU (and other resource) idle time due to IOlags.
Details in schedules: 
Macro Schedules: These schedules contain only the ordering of actions. They're key for ensuring data consistency.
Micro Schedules: These schedules offer more details, including precise timing and IO operations. They're key for optimizing performance.
Motivation: Macro Schedules are like to-do lists: they outline the dependencies of actions and their order, but don't specify when each action will be done. Micro Schedules are akin to calendar schedules: they provide not only the tasks and their sequence, but also precise timing, mirroring scheduled events in a day.
Note: Both serial and interleaved schedules have macro and micro versions. For simplicity, we'll call all these "schedules," and add descriptors only when needed for clarity. For example,
A schedule with interleaved actions is an interleaved schedule.
A schedule with interleaved actions and orderings is an interleaved macro  schedule. 
A schedule with interleaved actions and IOlag, locks and times, is an interleaved micro schedule.


Intuition for correctness of interleaved macro schedules
First, we’ll see some examples of serial and interleaved (macro) schedules, and gain some intuition for when interleaved schedules produce correct results.  In these examples, we assume start values are A = 10, and B=22. For simplicity, we also assume T1, T2, T3 decrement ‘x’ before W(x). I.e. x -= 1, to show a ticket purchase.
Start values: {‘A’ = 10, ‘B’ = 22}.

End values: {‘A’ = 9, ‘B’ = 20}.
Consider the serial schedule SS1 = T1 → T2 → T3. That is T1 runs first, T2 next, and T3 last. 
When we run this serial schedule, we see a ‘trace’ table of how A and B change with each read and write action, in each step. We also see a ``timeline’’ view, a visual version of the same trace information. 
We see that T1.R(A) reads A=10 in Step #1, (then decrements A), and writes T1.W(A) with A = 9 in Step #2. T2.R(A) reads A=9 and B=22 in Steps #3 and #4, and writes B=21 with T2.W(B) in Step #5.

End values: {‘A’ = 9, ‘B’ = 20}.
We see S1, an interleaved schedule. Notice that T2.R(A) is between T1.R(A) and T2.W(A). 

We also see how A and B change across steps. 

End values: {‘A’ = 9, ‘B’ = 20}.


We see S2, another interleaved schedule. Notice that it’s the same schedule as S1, with the addition of T2.W(B) to update B = 20. That is, the user buys a second ticket for B.

While S2 is also an interleaved schedule, it’s also an anomalous (or bad) interleaved schedule, because it’ll create data inconsistencies. 

Recall that T1, T2, and T3 need to be isolated from each other. 
Focus on T2’s perspective. T2.R(B) had 22 tickets, the user bought 2 tickets, one after the other, and B should end with 20 tickets. 
Focus on T3’s perspective. T3.R(B) reads in 21 tickets, decrements B, and T3.W(B) ends with 20 tickets.
In reality, B should end with 19 tickets because three tickets were sold, but B reflects only two tickets sold at the end. 

Intuitively, we see that T3’s Write(B) based on T2’s partially updated value of B created the problem, and the schedule lost an important decrement. That is, S2 creates data inconsistency.

In the next subsection, we’ll discuss how to analyze if a schedule produces correct or anomalous results.

Conflicts and Serializability Theory
Goal: Given an interleaved schedule such as S1 or S2, will it produce correct results?

Definitions
Conflicting actions (or conflicts) are pairs of actions from different concurrent transactions where
Both actions involve the same data item.
At least one of the actions is a write operation.
Example: T1.R(X), T2.W(X) are conflicting actions. Also, T1.W(X), T2.R(X) conflict, and T1.W(X) and T2.W(X) conflict.
Swapping non-conflicting actions is the process of reordering actions in an interleaved schedule while trying to achieve a serial schedule. 
Motivation: The idea behind these swaps is to transform the interleaved schedule into an equivalent serial schedule without altering the outcome of the transactions.
A Conflict Graph is a directed graph that represents the conflicts between different transactions in an interleaved schedule. In this graph, nodes represent individual transactions. For each conflicting action between two transactions, the graph has a directed edge from the node of the earlier action to the node of the later action.
Motivation: Simple data structure to help model and analyze conflicting actions.
Conflict-Serializable (CS) Schedules have conflicting actions ordered the same way as they would be in some serial execution. A schedule is conflict-serializable if and only if its corresponding conflict graph is acyclic.

Motivation: The ordering guarantees the outcome is equivalent to some serial schedule, ensuring consistency and correctness. Conflict serializability requires the conflict graph to be acyclic to ensure a valid serial schedule for transactions while preserving the order of conflicting actions. If a cycle exists, there is no way to execute transactions in a serial order without violating the order of conflicting actions.
Serializable Schedules are interleaved schedules that produce the same outcome as some serial schedule, ensuring consistency in the database. Serializable schedules are a super-set of CS schedules. 

Motivation: A serializable schedule can offer more performance speedups. However, it’s often harder to prove correctness, because we’ll need to prove that such a schedule produces the same outcome for all possible database values. By contrast, CS schedules offer provable guarantees for concurrent transactions based only on the order of conflicting actions and independent of the specific values in the database. Hence CS schedules are commonly used in practice to implement interleaved and correct schedules. CS schedules are a subset of serializable schedules. There are other classes of non-CS, but serializable schedules (for example, view serializable schedules you’ll learn in CS245, and we use similar techniques to prove serializability). 

Topological Sort is a general-purpose graph algorithm applied on directed acyclic graphs (DAG), producing a linear ordering of its nodes where for every directed edge U -> V, node U comes before V in the ordering.
Motivation: This technique is used to sequence tasks respecting their dependencies, meaning tasks can only be performed when all their prerequisites are completed. For transaction schedules, it helps produce a valid serial ordering for conflicting actions.


Analyzing our example interleaved (and serial) schedules

End values: {‘A’ = 9, ‘B’ = 20}.
Recall SS1, our serial schedule (also a trivial case of an  interleaved schedule). We can analyze this schedule by applying the above definitions. At the end of this section, you can also find example code for each of these steps.

We compute the conflicts. For example, T2 and T3 conflict on ‘B’ on steps #4 and #7. 
We see the corresponding Conflict Graph. We see nodes for T1, T2, and T3. We see edges for each conflict, including B-(#4, #7) from T2 to T3.
The Conflict Graph is acyclic, and is CS (conflict serializable). 
The schedule will produce output equivalent to T1 → T2 → T3. Of course this is the trivial case, because we started with a serial schedule, T1 → T2 → T3. 


End values: {‘A’ = 9, ‘B’ = 20}.
Consider S1, our 1st interleaved schedule.

We compute the conflicts.
We build the corresponding Conflict Graph. We see nodes for T1, T2, and T3. We see edges for each conflict, including B-(#4, #7) from T2 and T3.
The Conflict Graph is acyclic, and is conflict serializable. And therefore, S1 is serializable.
The schedule will produce output equivalent to running T2 → T1 → T3, or T2 → T3 → T1. This is because both are valid topological orderings in the Conflict Graph. 
We show one equivalent serial schedule, for T2 → T1 → T3. That is, we do T2’s actions first (in 1st 3 rows in the same order as in the MacroSchedule), then T1’s actions (in next 2 rows), and then finally T3’s actions (in last 2 rows). Conceptually, we are doing all of T2 in the same order (per the logic of T2.R(A) ->T2.R(B)->T2.W(B)), then all of T1 in the same order, and so on. 
In summary, S1 is a ``good’’ schedule. That is, it’s a conflict serializable schedule and will produce the same outcome as serial schedules T2 → T1 → T3, or T2 → T3 → T1. You can confirm the result from running T2 → T3 → T1 is identical to the result from running T2 → T1 → T3. 




Schedule is not Conflict Serializable. 
E.g., cycle [‘T2’, ‘T3’]
End values: {‘A’ = 9, ‘B’ = 20}.






Consider S2.

We compute the conflicting actions, and the Conflict Graph. 
The Conflict Graph is cyclic (e.g., cycle between T2 and T3), and is NOT conflict serializable.
Important to note: 
In general, a non-CS schedule may still be a serializable schedule. But often it’s hard to prove if a schedule is serializable, because we have to prove, for every possible data value, it produces the same outcome as a serial schedule. 	
However, a CS schedule will always have a serializable schedule.


Example code for Serializability algorithms 
In the Concerts Transaction Colab, we can run these algorithms live on real schedules. 

find_conflicting_actions identifies conflicting actions. It iterates through all pairs of actions in the macro schedule, checking if they are from different transactions, accessing the same variable, and at least one of them is a write. If these conditions are met, the actions conflict, and the conflict is added to a list. 

Builds the Conflict Graph, given a list of conflicts (from above). The function sorts the conflicts list based on transaction names and adds nodes and directed edges representing conflicts between transactions. The resulting Conflict Graph shows the relationships between conflicting transactions in the given schedule.

Generates an equivalent serial schedule from the given schedule if it is conflict serializable. It performs a topological sort on the conflict graph to obtain a serial order of transactions. Finally, the function combines the actions of each transaction to create the serial schedule.

If the Conflict Graph contains cycles, the schedule is not conflict serializable. 


Takeaways
Interleaved schedules for concurrent transactions can speed up system performance (next section) but pose problems due to potential conflicts between actions.
Conflict graphs visually represent conflicts between transaction actions.
Acyclic conflict graphs for a schedule guarantees conflict-serializability (and are therefore serializable) by avoiding circular dependencies between transactions. The outcome of such a schedule is equivalent to the outcome of a serial execution order.
Cyclic conflict graphs for a schedule implies it is not conflict-serializable. However, the schedule might still be serializable (recall serializable schedules are a super-set of CS schedules). But often it’s hard to prove if a schedule is serializable, because we have to prove, for every possible data value, it produces the same outcome as a serial schedule. 


Concepts 11.3
Locking protocols for interleaved micro schedules

Goal: Practical Lock-based algorithms to produce correct and fast schedules


Definitions
Concurrency control algorithms help manage concurrent access to shared data.
 
Motivation: These algorithms manage how transactions operate (a) while preserving data consistency, isolation, and correctness, and (b) with high levels of concurrency and efficient resource utilization.
Two-Phase Locking (2PL) divides each transaction into two phases:
Growth: The transaction acquires locks on data it needs but cannot release any locks. 
Shrink: The transaction releases locks but cannot acquire any new ones.
Strict Two-Phase Locking (S2PL) is a special case of 2PL, where the transaction retains all locks until the transaction ends (committed or aborted). All locks are released at once after the transaction ends.
Locks are data structures that concurrency control algorithms use.
Binary Locks are the simplest form of locks with only two states: locked and unlocked. A transaction must acquire the lock before accessing the shared data and release it when the access is complete.
Shared and Exclusive Locks (Read/Write Locks): Shared locks, or read locks, allow multiple transactions to read shared data concurrently, but not modify it. Exclusive locks, or write locks, allow a single transaction to modify the resource and prevent other transactions from accessing it during that time. 

Motivation:  Read/write locks would enable multiple users to concurrently read the number of available concert tickets without blocking each other, while still ensuring that only one transaction can modify the available_tickets at a time.



Theorem 2PL produces conflict serializable schedules

Intuition: If a transaction T1 precedes T2, and they have a conflict on ‘X’, T1 locks ‘X’ first. T2 can only proceed after T1 releases the lock (i.e., T1 is in shrink phase) The locking order aligns the conflicting actions’ order in the schedule with an equivalent serial schedule, where T1 is before T2.
Intuition by contradiction: Assume a non CS schedule adheres to 2PL. This implies a cycle in the conflict graph. For example, T1 depends on T2, T2 on T3, and T3 on T1. However, in 2PL, a transaction can't acquire new locks after releasing any, contradicting the circular dependency. Thus, the assumption is false, proving all schedules following 2PL are conflict-serializable.

In the below venn diagram, we see the set of possible schedules. Schedules produced by S2PL (aka S2PL schedules) are a subset of 2PL schedules, which are a subset of conflict-serializable schedules, which are a subset of serializable schedules. That is,
S2PL produces conflict-serializable schedules, because S2PL is a strict subset of 2PL.
2PL also produces serializable schedules. Conflict-serializable schedules are a subset of serializable schedules. 
 


Example S2PL code for Binary Locks
Let’s focus on S2PL concurrency control for binary locks, one of the four possible combinations among {2PL, S2PL}, and {binary, non-binary} lock types. The provided locking code can be easily adjusted to accommodate the other three cases.

The create_local_schedule function generates a ``local’’ schedule for one transaction’s Read and Write actions, as follows

IOlag: Each read action, R(x), has two parts - a Read-start (Rs(x)) and a Read-end (Re(x)). These two are separated by IOlag time units to model for the time it takes to perform the full read action. (Same with Write actions.)

Locking: For each variable, we model the locking process with three parts - a Request lock, a Get lock, and an Unlock. For this code, we assume S2PL for binary locks. (It’s easy to modify this code to support 2PL and non-binary locks as well.)

The create_serial_schedule function generates a serial schedule of actions for the given transactions.

In the provided Colab notebook, you will also find [optional] code to generate interleaved schedules, by reordering actions.

Example Serial and Interleaved Schedules

Example Serial Micro Schedule: In this example, we see three concurrent transactions, T1, T2, and T3 and their Read and Write actions with IOlag = 5 units. You can play with this example in Section 3.1 of Concert Transactions Colab. 



Serial schedule {T3 → T2 → T1}. Completion time = 48 time units (IOLag = 5 units)

We see a partial table (and timeline view) showing how the actions are mapped into a micro schedule with lock and read/write operations at specific time units, using the create_local_schedule function. The complete table can be found in the Colab notebook. 
For the given example actions Ops1 for Txns1, we present a serial schedule in (a):
We see T3's actions are run before T2's actions, then by T1's actions.
T1's R(A) and W(A) are converted into 
Req(A) and Get(A) for acquiring A's lock, Unl(A) for unlocking A.
Rs(A) and Re(A) for A's read-start and read-end. At Rs(A), the CPU requests the I/O device to read A's value from I/O (e.g., RAM). After IOlag time units, the CPU receives the value, as indicated by the shaded blue box, Re(A). The same process applies to Ws(B) and We(B).
Similarly, T2 and T3's operations are converted into Req and Get locks on A and B, and Rs, Re, Ws, We on A and B. Finally, Unlocks A and B.
The serial schedule runs from time slot 1 to 48. Notice that the CPU is only active for 25 slots out of the 48 slots. For the other slots, the CPU is idly waiting for some I/O, and wasting valuable resources. In this example, we used IOlag=5 time slots. In practice, IOlag will be much higher (e.g., in the 1000s or more). (We’ll see more examples with different IOLags shortly.)



Example Interleaved Micro Schedules: In below Examples (b) and (c), we observe two example interleaved schedules that achieve lower completion times of 31 and 45 time slots. Additionally, we see their Per-Transaction Locks and the corresponding WaitsFor graphs, which provide a concise representation of the transactions and the locks they are waiting for, along with the specific time intervals. 
For instance, in Example (b), we notice that T3 is waiting on T1 for A’s lock between time units 19-23 and T1 waits on T2 between 3-10. In Example (c ), we see T2.Req(A) at time=1, and T2.Get(A) only at time=38. T2 was unlucky with the CPU’s schedule choices, but the schedule is valid. Each time we run the scheduler, the CPU may make a different choice in execution. In Section 3.1 of Concert Transactions Colab, you can run the code to produce such interleaved schedules, and to compute WaitsForGraph.

(b) Example Interleaved schedule for Txns1, Ops1: Completion time = 31 time units



(c) Example Interleaved schedule for Txns1, Ops1: Completion time = 45 time units


Definition
Lock contention occurs when concurrent transactions request a lock on a shared value, and one or more transactions need to wait for a transaction to release the lock.
Motivation: It’s one simple measure of bottlenecks and which transactions are blocked. For example, specific Taylor Swift concert tickets and ticket zones likely had a lot of contention versus tickets sold to other concerts at the same time.   
WaitsFor graph is a directed graph that represents the lock dependencies between transactions in a concurrent execution schedule. In this graph, each node corresponds to a transaction, and a directed edge between two nodes indicates that one transaction is waiting for the other transaction to release a lock on a specific variable. The labels indicate the variable and the time units for the time span the transactions are waiting.

Motivation: 
Bottleneck identification and tuning: The graph visualizes dependencies and lock contention, enabling code optimization to minimize performance impact.
Deadlock detection and prevention: By analyzing the graph, developers can implement strategies to avoid deadlocks, such as lock timeouts or lock ordering.

Deadlock is defined as a state where two or more transactions are unable to progress due to circular dependencies on locked resources. Deadlocks can cause system stalls, leading to inefficiencies in resource utilization and transaction delays. Cycles within the WaitsFor graph signify deadlock situations.

Motivation: 
Deadlocks can cause system stalls, leading to inefficiencies in resource utilization and transaction delays.
A simple way to break deadlocks is to use a timeout-based approach. When a transaction is waiting for a locked resource for a specified period of time (the timeout), it is aborted and its locks are released. The aborted transaction can then be restarted at a later time. This technique allows other transactions to make progress by releasing the resources held by the timed-out transaction, thus breaking the deadlock cycle. However, this approach may lead to wasted work if transactions are frequently aborted and restarted.




Deadlocks with Interleaved Schedules
In contrast to the previously discussed interleaved schedules that efficiently executed transactions, we will now examine a deadlock schedule example. This schedule has transactions with overlapping resource requirements and lock acquisition order, potentially resulting in a deadlock. To better understand this situation, we will use the WaitsFor graph, which illustrates how the transactions are waiting for each other's locks to be released. 
Specifically, we see two interleaved schedules DS1 and DS2. In DS1, T1 and T2 both want locks to A and B, but end up deadlocking waiting for the other to release the lock. DS2 involves three transactions: T1, T2, and T3. Each transaction seeks to acquire locks on two variables. T1 wants to lock A and B, T2 wants to lock B and C, and T3 wants to lock C and A.



Deadlocked Schedule DS1





Deadlocked Schedule DS2

Speedup of Interleaved Schedules

Interleaved schedules provide a significant advantage over serial schedules. By allowing multiple transactions to execute concurrently, interleaved schedules can overlap CPU operations with IO operations, ensuring that the CPU remains busy while waiting for IO completion.

When the number of transactions increases and the IOlag is high, the potential for performance improvement through interleaving grows. For example, with 100 concurrent transactions and an IOlag of 100, we can achieve up to a 24.8x speedup over serial schedules.

Tradeoffs between Locking Algorithms



Two-Phase Locking (2PL)
Strict Two-Phase Locking (S2PL)
Phases
Expand and Shrink
Expand and Shrink
Lock Release
Can release locks before transaction ends
Holds all locks until transaction ends
Conflict Serializability
Guarantees conflict serializability
Guarantees conflict serializability
Cascading Rollbacks: If a transaction aborts (after making edits), it may lead to other transactions rolling back.
Possible, as locks can be released before transaction commits
Prevents cascading rollbacks, as all locks are held until commit. Also, a transaction in S2PL can't read uncommitted data from another transaction (due to the lock being held until commit).
Concurrency
Higher, as locks are released earlier in shrink phase
Lower, as locks are held longer, till the transaction ends


Takeaways on Transactions and Locking Protocols
Transactions: A transaction is a sequence of database operations (reads and writes) that must be executed atomically, consistently, isolated, and durably (ACID properties). In the Concerts example, a transaction might involve reserving a seat, updating the number of available tickets, and processing payment. These operations must be performed as a single unit to ensure data consistency, and avoid overbooking or incorrect seat reservations.
Strict Two-phase locking (S2PL): Strict two-phase locking (S2PL) is one popular concurrency control technique that ensures conflict serializability using locks. In 2PL, a transaction goes through two distinct phases: the growing phase, during which it acquires locks on resources (e.g., rows, tables), and the shrinking phase, during which it releases locks. S2PL is a stricter version of the 2PL algorithm where locks are held until the transaction ends. Many systems pick S2PL, for its simplicity and to avoid cascading rollbacks.



Case Study 11.4
Taylor Swift on TicketsDisaster versus TicketsFaster? 
Let’s analyze the Taylor Swift’s Concerts case study with some of the new tools we learned. 
Recall that the concert had 52 show dates (across different cities) and 3.5 million fans pre-registered for the Verified Fan Presale on Ticketmaster. About 1.5 million superfans received invite codes to buy tickets for November 14 at 10 am. The website got hit with a colossal 3.5 billion total system requests, which is four times its previous record!
The system was overwhelmed with many concurrent transactions (i.e., lock contention for popular tickets). With a popular artist like Taylor Swift, it’s likely more users wanted to buy tickets at the same time, contributing to high system load. Ticketmaster reports 3.5 billion total system requests, which is four times its previous record, but does not report transactions/second at peak time. To put it in context, it’s estimated that VISA’s global payment network manages an average of 110 million transactions/day or 100,000 transactions/second at peak times. 
Automated bot farms also compounded the problem by buying tickets, increasing the load and blocking genuine fans from purchasing tickets.
Let’s first focus on the first problem - we'll explore the user workflow and possible mitigation strategies. To understand potential design tradeoffs, we’ll simulate the user flow in two simpler sites, Ticketsdisaster.com and Ticketsfaster.com. We'll tackle the bot farm problems later.








Fan flow for Ticketsdisaster.com

Fan experience for TicketsDisaster.com (a simplified version)

Superfans were invited to buy tickets on a fine November day at 10 AM.
When the fan logged into the web site, the fan was placed in a virtual queue.
After waiting in the queue, fans were presented with a list of possible zones. The user picked a zone. If there were not enough seats for the fan and their friends, they were asked to pick another zone with availability. 
The fan was then presented with a list of seats in that zone.
The fan was then taken to a page to enter their payment information. The user was given a few minutes to review their order.
The fan clicked "Place Order." If the payment went through, the user was given their tickets. If the user clock ran out, the user had to reenter the queue or the zone selection phase. 

Problems from a fan perspective
Long Queues: Fans had to wait for hours in the virtual queue, behind thousands of other fans, and in some cases, buyer's remorse.
Group Booking Hassle: If there were not enough seats in a selected zone for a group, fans had to switch zones and retry. This added more load to the site and delayed the fans making a decision.
Slow System Response: The system became slow(er) with more load due to zone selection and payment processing. This led to more transactions failing.
Rushed Order Review: The short time limit for reviewing the payment information and order led to more payment and seat selection errors.



Alternate user experience for TicketsFaster.com (one example)


Invite superfans in advance to input their payment information, top zone preferences, date, and number of seats needed. Then, invite them to join the virtual queue on the specified sale date.
When the sale day arrives, position fans in a virtual queue as they log in.
Show each fan a list of possible zones that match their preferences. Auto-suggest ‘top 3’ recommended seats in that zone (e.g., user flow below)
With the pre-filled payment information, finalize the seats for the fan by clicking “Confirm Order.”

From a fan’s perspective
The number of fans in the virtual queue before you remains similar as before – this is a popular concert, and you can expect equally motivated fans to join the queue early.
The stress of entering preferences and payment information after a long wait in the queue is reduced, and the fan can do this on a less busy date.
On the peak sale day, the time spent on the site (and consequently, the load) by the average fan is lower.

From a systems’ perspective
Note that between Steps 3 and 6 in the previous user flow, the concurrent transactions have to retain locks on zones (and/or seats) until the user enters the payment information and the transaction was committed (or aborted due to a payment failure or timeout). This means that other fans couldn’t purchase or get an accurate count of the available seats for a specific concert and zone. Hence, the longer transactions held  onto locks, the higher the lock contention, leading to more fans waiting (i.e., a fan’s transaction is waiting for another transaction on the lock for the shared zone or seat). 
By collecting preferences and payment information on a less busy day, the system can better allocate its resources for quicker fan request servicing on peak day.   
   




Takeaways for high load transaction systems
Transaction Simplicity and Convenience: Transactions are an effective and popular method for various data applications. However, they may become a bottleneck when there are prolonged lock times or lock contention in high performance applications.
Redesign User Flows to Reduce Lock Contentions: Look for ways to redesign the user workflow to hold locks for shorter durations. For example, maintaining locks on key data for minutes while a user fills in payment information can significantly delay transactions. Also, maintaining seat-level locks (versus zone-level locks) could reduce lock contention, if you have 100s of seats per zone, because fewer user transactions will wait on the same locks. That is, when possible, use higher-resolution locks. 
Consider Alternate, Non-lock-based Schemes: Explore other methods that don't rely heavily on locking mechanisms. For instance, accept a user request with a timestamp and asynchronously confirm the request, provided the user is amenable to receiving a later confirmation. This approach can help alleviate lock contention and improve system performance. That is, use the timestamp to maintain the fan’s relative order when they logged in, and use that order to execute transaction preferences. In general, there are many more locking schemes, with various performance and latency tradeoffs. For a deeper understanding of these advanced techniques, please review Gray and Reuter’s classic. These will be covered in a more advanced data system class. 



Case Study 11.5
Logging for recovery

Goal: Learn how to recover a database after a systems crash with LOGs


Definitions
Systems Crash: Refers to a sudden, unexpected failure that interrupts the database's normal operation. This includes hardware problems such as disk crashes, memory corruption, power failures, network failures, or denial of service and security attacks, or software issues like bugs, and running out of RAM or disk resources. 

Write-Ahead Logging (WAL): A technique to support the Atomicity and Durability properties of ACID. When a transaction runs and makes changes, WAL writes UNDO/REDO records in a separate LOG (a special DbFile) before modifying the database. For example, a simple UNDO/REDO record will contain <TransactionID, Timestamp, Variable, OldValue, NewValue>. E.g., <T1, <time>, ‘B’, 22, 19.3> to show that T1 changed ‘B’ from 22 to 19.3.  
UNDO/REDO records (aka OLD/NEW records): The UNDO part of the record keeps track of the original (i.e., old) value before any changes are made. If a transaction ABORTs, the system can revert to the original state using the UNDO. The REDO part of the record tracks the updated (i.e., new) value from the transaction. If a transaction COMMITs, and the system crashes later, the system REDOes the changes for that transaction during recovery, ensuring that the database reflects all COMMITed transactions. 

Recovery: The process of restoring the database to a correct and consistent state after a failure. When the system comes back online after a failure, it goes through the WAL and REDOes updates from all COMMITed transactions. This process can also involve UNDOing updates from ABORTed transactions. As part of this, transactions that did not COMMIT pre crash, will also be ABORTed.

Motivation: Recovery with WAL ensures that even if a system failure occurs, all COMMITed transactions can be recovered using the WAL, thus maintaining Durability. In addition, COMMITed transactions are fully redone, and no partial changes from Aborted transactions are reflected in the database, thus maintaining Atomicity.

For concert transactions, here's a simple example of how WAL and recovery might work:
User Interaction: A user decides to buy a concert ticket and clicks the "Buy" button, initiating a transaction.
Write Ahead Logging (WAL): Transaction details (user ID, concert details, ticket price, etc.) with UNDO/REDO records are first logged in the WAL, ensuring all intended changes are recorded.
Database Update: The database then reflects the transaction. It reduces the ticket availability by one and assigns the purchased ticket to the user.
System Crash: Suppose the system crashes immediately after the transaction. The ticket count has been reduced in the database, but the assignment of the ticket to the user may be in question due to the crash.
Recovery: Upon system restart, it undergoes recovery. Using the WAL, it locates the user's ticket purchase transaction and cross-checks the database to confirm the transaction's completion. If the database shows the ticket count decreased but not assigned to the user, the system redoes the transaction, ensuring the ticket's assignment to the user. If the transaction couldn't COMMIT (e.g., double booked on a phone call), the system undoes the transaction, increases ticket availability, and issues a user refund.
Long-Running Transactions: In parallel to user interactions, the event organizers may adjust ticket prices for all seats and zones by 10%. In this bulk operation (spanning many database rows), each price change is logged into the WAL  before being applied to the database. If a system failure occurs during this operation, upon recovery, the system uses the WAL to identify which tickets have been updated (so their prices don’t increase by 10% again) and continues from where it left off. In the event that the operation can't be completed (e.g., crash or developer aborts partway through), the system reverts any changes, restoring the original ticket prices.

WAL’s Ordering Rules

WAL uses two rules to order the WAL and database updates to ensure atomicity and durability
Rule 1: Time(WAL(x)) < Time(We(x)): Before a transaction finishes writing the new value of 'x' to the database (We(x) or Write-end(x)), it must first log the UNDO/REDO record for 'x' to the Write-Ahead Log (WAL(x)). Logging this information before making changes to the database ensures that if a failure occurs, we can either UNDO the changes (if the transaction is later aborted) or redo the changes (if the system crashes before the changes are written to the database).
Rule 2: Time(WAL(x)) < Time(Commit/Abort): Before a transaction can end (Commit or Abort), it must log the UNDO/REDO rows for all the values it changed. 
So for each 'x' that the transaction modifies, the timestamp of the WAL log for 'x' (Time(WAL(x))) must be earlier than the timestamp of the transaction's end (Time(Commit/Abort)). Logging the UNDO/REDO rows for all values ensures that if a crash occurs after the transaction ends but before its changes are written to the database, we can still recover the correct state of the database based on the WAL. 
Finally, write the TXN’s final commit/abort state into WAL just before releasing all the locks and TXN commits/aborts (and notifies the user). We will also see later, during recovery, that a transaction is considered Aborted If there is no COMMIT row in WAL.

With these flexible rules, WAL can optimize writes and improve performance.
Batching of WAL(x): When a transaction updates several values, it generates UNDO/REDO rows for all these values. The database system can append these logs to the WAL in a single batch operation, which is generally faster than writing each log separately. Batch writes are particularly efficient for disk-based storage systems, as they can make good use of the disk's sequential write bandwidth. This reduces the time that transactions spend waiting for their logs to be written, leading to faster transactions.
Deferred We(x): By logging the UNDO/REDO information before writing the new values to the database, the WAL protocol allows the database system to defer the actual database writes (We(x)) until a later time. This can be a significant performance advantage because it reduces the number of random disk writes. When there are other updates to the same IO page, the database can write out the page once, rather than once per update. 

Overall, by enabling efficient batch writes and reducing the number of random writes, the WAL protocol can help a database system achieve high performance while still ensuring the atomicity and durability of its transactions.

Next we discuss some basic examples to introduce WAL. In Transactions Colab, we show one simplified implementation of WAL and more detailed examples. Here, we use 100 lines of code to capture a simpler version of the above rules, which is correct, but could be further optimized with more careful code.

When a transaction Writes a value, WAL updates these data structures. 
RAM log: This in-memory log records the changes a transaction makes to variables. It is used for quick access and ‘’UNDO’’ of changes for ABORTs.
WAL log: This persistent immutable log (i.e., older entries are never updated) appends (a) all UNDO/REDO records, and (b) each transaction’s COMMIT/ABORT state. In this code, we follow WAL’s Ordering Rule1 in process_schedule’s Ws and We steps and Rule2 at the end of the commit_or_abort  step.

When a transaction ends
If the transaction needs to ABORT, all changes made by this transaction in the RAM_state and the DB_state are UNDOne. 
If the transaction COMMITs, the changes are eventually reflected in the DB_state. 




Example 1: 1 Transaction updating 2 values
# values of A and B in the DB
db_state = {'A': 19, 'B': 23} 
ops = [
   ("T1", "R", "A"),
   ("T1", "R", "B"),
   ("T1", "W", "A"),
   ("T1", "W", "B"),
]


Let’s first study a single transaction, T1, reading and writing A and B.

In the below table, we see the WAL (in gray/white) with the UNDO/REDO records and COMMIT/ABORT states.

In addition, we show a ``trace’’ of data states (in color) at each step. These trace columns are not stored in the WAL Log. We use these to help you with intuition. 
DB_state: The current (and durable) data in the database (in blue).
RAM_state: Data currently in RAM, not yet persisted (in red). 
RAM_log: Temporary log in RAM for active transactions (in red). 
Also, recall that RAM is volatile, and both RAM_state and RAM_log (in red) may be lost in a system crash. 


For example, when A is updated from 19 to 22.8, this change is reflected in the RAM_state and RAM_log in timestamp=16, while the DB_state still has the original value. 
By timestamp=21, the DB_state reflects A=22.8. As you can see, DB_state could reflect an update even before the transaction commits. Notice that this is consistent with WAL ordering rules #1 and #2 – there is no constraint between Time(We(X)) and Time(Commit/Abort) in the WAL ordering rules. (Why? This helps the DB reorder its IOs for better performance, without compromising correctness.)
By timestamp=26, the DB_state reflects the updated values of both A and B.



Example 2: 1 Long-running Transaction updating many values

db_state = {'A1':19,'A2':32,'A1000': 27}


schedule2 = [
('TLong', 'Req(A1)', 'A1', 1), 
('TLong', 'Get(A1)', 'A1', 2),
('TLong', 'Ws(A1)', 'A1', 3), 
('TLong', 'We(A1)', 'A1', 10),
('TLong', 'Req(A1000)', 'A1000', 80),
('TLong', 'Get(A1000)', 'A1000', 81), ('TLong', 'Ws(A1000)', 'A1000', 85),
('TLong', 'We(A1000)', 'A1000', 90), ('TLong', 'Unl(A1)', 'A1', 1000)]
In this example, we see a transaction, TLong, updating thousands of values (e.g., increasing prices of seats by 20%) over 1000s of time slots. The transaction's progress is tracked partially through variables A1, A2, and A1000. We see two cases below
TLong Commits: A1 gets updated to 22.8 at time slot 3 and is written to the database by time slot 85.
TLong Aborts: If the transaction ABORTs (e.g., systems crash or the app developer aborts part way through), we UNDO changes to A1, A1000 to their original values. We add W-abort records and the final record stating TLong ABORTed in the WAL Log.
Takeaways: 
Note that some values are updated in the database before the transaction COMMITs. (e.g., A1’s 22.8). This is crucial in long-running transactions that can fill up RAM space, and require periodic saving of partial changes.
When a transaction ABORTs, the database UNDOs any partial changes and restores the original values. That is, the updates are atomic.


transaction_execute_schedule(db_state, schedule2, {'TLong': "commit"})



transaction_execute_schedule(db_state, schedule2, {'TLong': "abort"})



Intermediate: Logging + Locking for multiple concurrent Transactions – Full picture

So far, we saw examples of LOGs with 1 transaction. Let’s now consider concurrent transactions with shared variables. While the focus will continue to be on LOGs, we’ll see a fuller picture of how TMs run concurrent transactions (with S2PL). 
Specifically, we’ll see T1, T2, T3 updating ‘A’, ‘B’, ‘C’. The TM may use S2PL (or other concurrency algorithms) and compute a micro-schedule.  We’ll focus on the TMs logs. In the Colab, you can see the micro-schedule with its Locks and IO actions, and also experiment with other COMMIT/ABORT sequences.
Example 3: 3 Transactions updating three shared values

db_state3 = {'A': 19, 'B': 32, 'C': 27}


# Schedule of operations
ops3 = [
   ("T1", "R", "A"),
   ("T1", "W", "A"),
   ("T2", "R", "A"),
   ("T2", "W", "A"),
   ("T3", "R", "B"),
   ("T3", "W", "B"),
   ("T3", "R", "C"),
   ("T3", "W", "C")
]


We see two scenarios of TXNs commits and aborts below. 
T1, T2, T3 commit: T1 and T2 share ‘A’, and ‘A’ is updated to 22.8 and 27.36 in the DB in stages.
T1, T2 commit, while T3 aborts: We see ‘B’ is updated to 38.4 in the DB by time=23. And ‘C’ is updated to 32.4 in DB by time=28. However, at time=28, T3 needs to be aborted (e.g., the developer CTRL-Cs T3). We add W-abort records and the final record stating T3 ABORTed in the WAL Log, and undo T3’s changes. Meanwhile, T1 and T2 can still COMMIT, independent of T3.
Takeaways: 
Note that values could be updated in the DB before the transaction COMMITs. (e.g., B’s 38.4 or C’s 32.4). 
When a transaction ABORTs, the database UNDOs any partial changes and restores the original values. That is, the updates are atomic.





In Transactions Colab, we dig into examples of real-world transaction scenarios. We’ll use the Colab because the associated WAL logs are more detailed. 
Multiple Transactions: We explore instances where multiple transactions update various values. We present outcomes where all transactions commit successfully, and also where a few transactions abort.
Impact of System Crashes: We see how system crashes affect the database's state and the possible inconsistencies they can introduce.
Recovery: We guide you through the process of restoring the database to a consistent state after a system crash, leveraging the WAL Logs.
Handling Repeated Crashes: We take on more challenging situations, such as dealing with consecutive system crashes. 

Intermediate: Crash and recovery 

WALRecovery handles crash recovery by UNDOing ABORTed transactions and preserving COMMITed ones. This class includes the following methods:
recover: Scans the log and UNDOs any transactions that were marked as ABORTed, making sure to reflect the state of the database and the RAM at the given timestamp. It marks the crash and restart times in the log for reference.
epoch_recover: Start the recovery process from the last system restart timestamp, or from a provided timestamp, whichever is later. This is to ensure that it does not unnecessarily recover transactions from before the last successful system restart.
crash: Simulates a system crash at a given timestamp. It resets the RAM state and log, marks non COMMITed transactions as ABORTed, and restores the database state to the last known state before the crash.


Parallels between WAL and Blockchain [Optional]
Write-Ahead Logging (WAL) and Blockchain both offer mechanisms for ensuring data integrity, but they do so in different contexts, using similar core ideas, but with different techniques.
Similarities:
Immutability: Both WAL and blockchain maintain immutable logs of operations. 
Durability: Both provide mechanisms for reliable data recovery and audit trails.
Recovery: Both systems can restore their state by replaying the logs.
Differences:
System Design: WAL is for centralized databases focusing on crash recovery. Blockchain is decentralized, maintaining consensus across many nodes.
Confidentiality: WAL-based databases control access to private data. Public blockchains make transactions visible to all participants.
Concurrency Control: WAL manages simultaneous transactions internally. Blockchain avoids conflicts via distributed consensus mechanisms.
Data Structure: WAL is a linear log, while blockchain is a linked list of blocks with a hash reference to the previous block.
In summary, while WAL and blockchain both provide mechanisms for ensuring data integrity and recovery, they are designed for different use cases. WAL is primarily used for crash recovery in centralized database systems, while blockchain is used for maintaining a consistent, distributed ledger in a decentralized network.

Takeaways
Write-Ahead Logging (WAL): Each transaction’s changes are first 'logged' in a dedicated place before being applied to the database.  
Transaction Atomicity, Data Durability: WAL helps maintain the atomicity of transactions. If a system fails in the middle of a transaction, the WAL aborts (or ``rolls it back’’, or ``reverts,’’ or ``undoes’’) during recovery, ensuring that a transaction appears as entirely executed or not executed at all. Also, by logging changes before they are applied to the database, WAL ensures that no data is lost.
Handling Long-Running Transactions: For long-running transactions that span hours and modify many data entries, WAL ensures intermittent changes are logged and persisted, thereby preventing loss due to limited RAM space or resources.

Case Study 11.6
How does NanoDB build transactions? [Optional Code]

Goal: Put together Locks, S2PL, and WAL for transactions



The Transaction class represents an individual transaction in the system. Interacts with a TransactionMgr instance to manage locks, and to log transaction events. 

In this implementation, we assume each transaction reads and modifies one value, and gets one lock for that value, for simplicity. (We can extend this code to multiple variables and locks, with a little bit of work.) 
Begin starts a transaction by acquiring a lock for a given lockname using the Transaction Manager's get_lock method.
Commit method releases the lock for the transaction and adds the UNDO/REDO log and "COMMIT" outcome.
Abort method also releases the lock associated with the transaction, but adds the UNDO/REDO log and “ABORT” outcome to the WAL log.





The TransactionMgr class is responsible for managing locks and logs. It maintains data structures to store logs for the transactions, and the current locks held by each transaction. In addition, we track the lock_sequence of lock acquisitions/releases for our convenience to debug the sequence.

The get_lock method acquires a lock for a given transaction_id and lockname. It first ensures that the lock for the given lockname exists, and then acquires the lock. 

The release_lock method releases the lock for a given transaction_id. It retrieves the lockname associated with the transaction_id, releases the lock, and removes the lockname entry for the transaction_id. 

The add_to_log method adds transaction details to the transaction_log list, which stores information about each transaction's outcome, old value, new value, and result.

Case Study 12.1
How to track user’s Spotify activity with high speed LSM trees in systems like BigTable and Cassandra? 

Goal: Design hybrid data structures for special classes of high read/write applications     

Let's consider the problem of tracking user's play counts and likes for each song in Spotify. This is a high-write-volume operation as there are millions of users who are constantly engaging with Spotify and rating different songs. In Section 2, we discussed how LSM trees can help with high volume writes. We now discuss how LSM trees can also help with concurrent updates. 

Tradeoffs between LSM trees and locking-based writes
Recall from Section 2 that Log-Structured Merge-Tree (LSM tree) is a hybrid data structure for providing indexed access to files with high insert volume, such as user activity. It was designed to handle random writes efficiently, which is a weak point for many traditional data structures like B-trees.
An LSM tree combines three ideas we learnt in the past few sections: (a) buffer random write operations and organize them into large, sequential disk LOG-based writes, (b) keep underlying data stored in sorted order of keys, and (c) build an index over the sorted data.

Locking-based in-place updates
Consistency: Changes are immediately reflected and available for querying. This is an advantage when strong consistency is required.
Performance: The need to lock and unlock data for every update can slow down the system, especially when dealing with high volumes of data.
Contention: High contention can occur with many concurrent updates, leading to performance bottlenecks.
Random Writes: Constant random writes can increase latency and decrease the lifespan of the underlying storage medium.
Scaling: Scaling for large volumes of data can be challenging due to the above factors.


LSM Trees
Consistency: May provide weaker consistency compared to in-place updates, as changes may not be immediately available for querying. This can be a trade-off worth accepting in scenarios where high write throughput and scalability are more important than immediate consistency.
Write Efficiency: Designed to handle high write loads efficiently. Changes are first stored in an in-memory table and then flushed to disk in a sorted manner. This reduces disk I/O operations and avoids lock contention.
Read Performance: Read operations can be more efficient over time due to the compaction process, which periodically merges and discards redundant data.
Scalability: Better suited to handle large volumes of data due to high write throughput and improved read performance over time.
Example use case: Concert tickets.

Consistency Requirement: In a concert ticketing system, it is essential to maintain high consistency to avoid overselling. Once a ticket is sold, the available count should be immediately reduced to reflect the current state of availability and visibility to all users. In-place updates offer strong consistency which is critical in such scenarios.
Concurrency Control: There could be high concurrent demand for the same tickets. Locking-based updates help ensure that tickets are sold to one user at a time, avoiding situations where multiple users purchase the same ticket.
Low Write Volume: Unlike a use case such as user activity logs, the volume of writes (ticket sales) in this scenario might not be as high, making the write efficiency advantage of LSM Trees less significant.
Example use case: User activity.

Performance: Given the high volume and velocity of user activity logs, the high write throughput and scalability offered by LSM Trees are advantageous.
Consistency: The consistency trade-off with LSM Trees might be acceptable, as it may not be crucial for user activity logs to be immediately queryable after they are written. 
Clustering: The improved read performance of LSM Trees after compaction can be beneficial for generating user recommendations and understanding user behavior, which would frequently involve reading historical user activity data.

Optional code for LSM trees






Case Study 12.2
How does Google Docs work for collaboration? 

Goal: Learn how some consumer applications use transactional principles

Google Docs allows users to create and edit documents online while collaborating in real-time with other users. The user’s browser sends requests to the server, which then processes the requests and sends back the appropriate response for the browser to display. On the server side, Google Docs uses a combination of technologies to store, process, and serve documents to users. The serving, storage, and indexing challenges are similar to our prior case studies.
In this case study, we’ll focus on collaboration with multiple users editing the same doc. For example, suppose two users, Alice and Bob, are editing the same document simultaneously. Alice inserts the word "quick" at position 10, while Bob deletes the word "fox" from position 5. Alice and Bob are concurrent users. However, we would not want to ‘lock’ a document, nor a paragraph, nor a line to let concurrent users edit. That is, we need more than the binary and non-binary locks we’ve seen. 
Operational Transforms
One way to build the collaboration backend in Google Docs is to use Operational Transformations (OT). OT is a method for resolving conflicts that arise when multiple users are editing the same document concurrently. OT is based on the principle of transforming operations so they can be applied in any order yet produce the same end result. It relies on the concept of commutativity (operations that can be rearranged without changing the outcome), but it achieves this commutativity through transforming the operations. When a user makes a change, the operation is sent to the server, which then applies the operation to the document's current state. The server also keeps track of the operations made by each user and sends them to other users who are currently viewing the document. The browser application then applies the incoming operations to the document, resulting in a real-time collaboration experience.

Example 
Alice and Bob are working on the same Doc that reads: "The quick brown fox." Alice decides to change "quick" to "speedy", and Bob decides to add "jumps over the lazy dog" at the end. They make these changes at the same time. Later, Alice decides to add "quickly" at the end of the document, and Bob decides to replace "fox" with "hare".
Time
Alice's Log
Bob's Log
t1
OP_Alice: Replace("quick", "speedy") at position 4
OP_Bob: Insert(" jumps over the lazy dog") at position 19
t2
Transformed_OP_Bob: Insert(" jumps over the lazy dog") at position 21
Transformed_OP_Alice: Replace("quick", "speedy") at position 4
t3
OP_Alice: Insert(" quickly") at position 45
OP_Bob: Replace("fox", "hare") at position 16
t4
Transformed_OP_Bob: Replace("fox", "hare") at position 16
Transformed_OP_Alice: Insert(" quickly") at position 47
t5
Document State: "The speedy brown hare jumps over the lazy dog quickly."
Document State: "The speedy brown hare jumps over the lazy dog quickly."





Time t1: Initially, Alice replaces "quick" with "speedy" at position 4, while Bob inserts " jumps over the lazy dog" at position 19.
Time t2: Alice receives Bob's operation. Because Alice's change affected the length of the document before Bob's insertion point, Alice applies Bob's operation at position 21. Bob receives Alice's operation and applies it directly, because Alice's change doesn't affect Bob's operation's position.
Time t3: Alice inserts " quickly" at position 45, and Bob replaces "fox" with "hare" at position 16.
Time t4: Alice receives Bob's operation, which doesn't affect the position of her change, so she applies it directly. Bob receives Alice's operation, which does affect the position of his change due to the length change of the document, so he applies Alice's operation at position 47.
At the end of this sequence, both Alice and Bob see the same text: "The speedy brown hare jumps over the lazy dog quickly."

Conflict-Free Replicated Data Types (CRDTs)
Conflict-free replicated data type (CRDT) is a data structure that can be replicated across multiple nodes, and automatically merge conflicting updates made to the same document. They define data types where all operations are commutative by nature. CRDTs are designed to ensure that all replicas of the data structure eventually converge to the same state, regardless of the order in which updates are made or which replica the updates are made on.
A distributed counter is one of the simplest examples of a CRDT. In a CRDT-based system, we might define the counter as a set of (node, value) pairs, where each node independently increments its own value. The total value of the counter is the sum of all values. If Alice's node increments the counter, it increments its own value in the pair. This operation commutes with any other increment operation, because each node is only updating its own value. When you look at the operation log in a CRDT system, you'll see that operations from different nodes can be applied in any order and still lead to the same final state. CRDTs can be used in various types of distributed systems such as distributed databases, real-time collaborative text editors, and distributed cache systems.


Takeaways for LOGGING (12.1, 12.2)

Consistency and Recoverability: Logging is a vital technique for ensuring data durability, atomicity, and system recoverability. In Write-Ahead Logging (WAL) we saw how changes are logged before they are applied, which helps recover the database to a consistent state after a crash. Similarly, Google Docs' OTs log every operation, enabling real-time synchronization and facilitating recovery of document state.
Immutable Audit Trails: Logging provides an immutable history of all transactions, making it useful for auditability and traceability. For example, in WAL and blockchains we only append new entries to the log, and never alter old entries. With such logs, its easy to trace back what happened with any row. For example, how was a row modified, when, and by which transaction.  
Concurrency and Collaboration: Logging is another key tool to enable concurrent operations and collaborative work. Google Docs' OTs, for instance, allow multiple users to edit a document simultaneously, logging each operation to ensure users see the same view of the document. WAL allows concurrent transactions by maintaining log records for each transaction.

Remember, while logging contributes significantly to system reliability and auditability, it also introduces overheads such as increased storage requirements and potential performance trade-offs due to the need to write logs. However, the benefits often outweigh these costs in systems where data integrity, recoverability, and auditability are paramount.



5. Distributed Systems
 
Concepts:  Distributed systems – communication, replication, etc.

Colab: Distributed Systems colab
Learning Goals
Communication using MessageQueues
How Google Ads system evolved from ten replicated MySQL DBs to F1’s distributed SQL engine? 
How Discord scales to trillions of messages?
Exercises 



Concepts in Section: Why Distributed Systems?
Distributed systems help us tap the power of tens to millions of interconnected machines, extending the capacity and performance beyond what a single machine or disk can provide for big data problems. The main goals of such systems include
Scalability: As applications and data grow, distributed systems can accommodate this growth by adding more machines and disks (aka nodes) to the system. This approach helps maintain system performance and manageability as the data and user base increase.
Availability: Distributed systems are designed to be fault-tolerant, ensuring that the system continues to operate even if one or more nodes fail. By replicating data across multiple nodes, distributed systems can maintain data availability and prevent data loss during hardware failures or network outages.
Performance: By distributing data and processing across multiple nodes, distributed systems can handle more requests and perform complex operations faster. This is particularly important for applications with high throughput and low latency requirements, such as real-time analytics, gaming, or financial services.
Reliability: Distributed systems can provide a higher level of reliability by distributing the risk of failure across multiple nodes. This reduces the likelihood of a single point of failure causing the entire system to become unavailable.
For instance, consider a distributed system with 3-way replication, where each data row is stored on three different machines to achieve performance, reliability, and fault tolerance. With three replicas of each data row, we can request the data row from any of the machines. However, when updates occur, we need to address several challenges: (a) handling cases when some replicas are down, (b) ensuring reliable communication of update messages to replicas even when parts of the network may be down, and (c) dealing with scenarios where two machines are alive, and the third is unreachable or in an inconsistent state.

Common design concepts in distributed systems
Data Replication and Partitioning: Replicating data involves storing multiple copies of data across different nodes to increase fault tolerance, availability, and read performance. Partitioning (sharding) data distributes it across multiple nodes based on hashing, range partitioning, or other custom strategies. This approach enables load balancing of incoming queries, optimizing resource utilization, minimizing response times, and preventing overloading individual components.
Motivation: Splitting data across multiple nodes improves system performance, resilience, and scalability.

Consensus Algorithms: These algorithms ensure that a group of nodes can agree on a single value or decision, even in the presence of failures or network partitions. 

Motivation: Maintain a consistent shared state across nodes, despite failure.s

Examples: Here's the intuition behind one simple consensus algorithm. One machine becomes the leader, and the others are followers. If there's no leader, the machines elect one. The leader takes charge of managing and updating the shared state (LOG) for the entire system. Followers listen for updates from the leader and apply those updates to their local copies of the shared state. If the leader fails (or becomes invisible to other nodes), the remaining machines hold another election to choose a new leader and continue the process. Raft is one popular consensus algorithm that helps multiple machines in a distributed system agree on a shared state. Older systems also use Paxos, a popular but more complex consensus algorithm.

Publish/Subscribe Pattern: This communication pattern involves components publishing to specific topics while other components subscribe to these topics to receive updates. This method enables efficient dissemination of requests and updates, reducing communication overhead. 

Motivation: The Publish/Subscribe pattern improves reliable communication across nodes by reducing overhead and helping efficient event dissemination.

Examples : We’ll discuss tools like Kafka and Amazon's Simple Queue Service in Case Study 14.


Common design trade-offs in distributed systems
Consistency:
Strong Consistency: In a strongly consistent system, write operations must be acknowledged by all replicas before being considered successful. Consensus protocols (e.g., Paxos, Raft) ensure a majority of replicas agree on updates. This guarantees subsequent read operations return the most recent write. However, strong consistency comes at the cost of increased write latency and reduced availability during network partitions or node failures.
Motivation: Strong consistency provides predictable data access and guarantees that clients always see the latest data, which is important for applications that require strict data integrity.
Weak Consistency: In a weakly consistent system, write operations can be acknowledged by one or more replicas without immediate agreement from all. Updates propagate asynchronously, eventually bringing all nodes to a consistent state. This approach prioritizes availability and performance but may result in temporary data inconsistencies.
Motivation: Weak consistency trades some data integrity for improved performance and availability, which can be suitable for applications where occasional stale reads are acceptable.

Availability:
High Availability: A highly available system with 3-way replication ensures operation even if one or more replicas fail or become unreachable. Load balancing mechanisms maintain performance by distributing requests evenly across replicas. However, high availability may require relaxing consistency guarantees, leading to temporary data inconsistencies.
Motivation: High availability ensures continuous operation, which is crucial for mission-critical applications where downtime is unacceptable.
Partial Availability: A partially available system with 3-way replication continues operating even if some replicas become temporarily unavailable, providing limited functionality during failures or network partitions. Trade-offs include the possibility of reduced system performance, functionality, increased latency, and stale data.
Motivation: Partial availability provides a balance between continuous operation and resource usage, suitable for applications where occasional service degradation is acceptable during failures or network partitions.

Partition Tolerance: A partition-tolerant system functions despite arbitrary partitioning due to network failures. It continues operating even if a node goes down or a network partition occurs, ensuring the system can function in the face of failures.
Motivation: Partition tolerance is essential for building resilient distributed systems that can withstand network failures and continue to function, which is vital for applications that need to operate in unreliable environments.

Brewer’s CAP theorem states that it is impossible for a distributed system to guarantee Consistency, Availability and Partition tolerance simultaneously. Per Brewer, a system can only provide up to two of these guarantees at the same time. For example, a system that prioritizes availability and partition tolerance may not be able to ensure consistency. 
The CAP theorem has been a subject of controversy since it was first introduced. Some argue that the theorem oversimplifies the trade-offs in distributed systems and that it is not always possible to make a clear distinction between consistency, availability, and partition tolerance. Despite these criticisms, the CAP theorem remains an important concept for gaining intuition behind key trade-offs in distributed systems. 

Takeaways
Distributed systems use common patterns like data replication and partitioning, consensus algorithms, and publisher/subscriber communication, to solve common challenges in managing data consistency and reliability.
Distributed systems need to tackle design tradeoffs between Consistency, Availability, and Partition tolerance. 
Modern data apps have diverse needs. Different solutions in the market pick different points along the trade-off spectrum based on the specific use cases they aim to serve.


Case study 13
Distributed Database Systems: Decouple Ticket Purchases,  Scalper Detection and Attack Mitigation

Goal: See examples of how components of a distributed system communicate 


In addition to ticket sales, for popular concerts we often need to handle other facets, such as
Ticket Scalping when individuals or entities buy large quantities of tickets and then resell them at inflated prices, exploiting the high demand for tickets. This activity can lead to a poor experience for genuine fans unable to purchase tickets at face value.
Denial of Service (DoS) Attacks, when attack bots flood the target system with a high volume of requests, making it unable to process legitimate user requests, especially when tickets are released for sale.
A publisher-subscriber model with message queues can help address such issues by decoupling the ticket purchase processing from the fraud and attack detection systems. When a ticket purchase occurs, we use a message queue to store incoming requests. The system can process requests at a controlled rate, reducing the likelihood of being overwhelmed by a sudden influx of concurrent traffic. Additionally, multiple subscribers can consume the requests and handle different actions, such as validating requests, storing purchases in a database, or performing ``outlier’’ detection for botnets or fraud.


Here’s a sample implementation of a MessageQueue (using SQLite) to showcase the main functionality. You can play with this example in the Distributed Systems colab.

Producers will enqueue (publish or pub) requests, and consumers can dequeue (subscribe or sub) requests for processing. Often, the requests pub-sub on specific #topics (e.g., purchase tickets, notify user). 

In practice, popular MessageQueue packages (such as Kafka or RabbitMQ) or services (like AWS Simple Queue Service) will offer highly optimized enqueue and dequeue data structures.




Here’s an example producer requesting ticket purchases. 

Here’s an example of a consumer acting on ticket purchases.


Concepts
In general, scaling distributed systems involves increasing their capacity to handle larger volumes of data and higher query loads. There are two main approaches to scaling: data partitioning and functionality-based partitioning.
Data partitioning, also known as sharding, involves dividing the data across multiple servers, with each server responsible for a subset of the data. For example, partition Taylor Swift concert sales for different venues from other ticket sales. This approach allows the system to distribute the workload and queries among the nodes, enabling near-linear scalability and improved fault tolerance. Since the failure of one node does not affect the entire system, data partitioning is suitable for handling massive amounts of data and high query loads in distributed databases.
Functionality-based partitioning, on the other hand, focuses on dividing the system based on the different functionalities or services it provides. Each server or group of servers is dedicated to a specific function or service, such as data processing and transactions, fraud detection or recommendation systems. This approach enables better resource allocation, improved performance, and easier maintenance, as each component can be independently scaled, deployed, and updated. Functionality-based partitioning promotes a modular and maintainable system architecture, allowing developers to add or modify features with minimal impact on the overall system.
Message queues play a crucial role in both data partitioning and functionality-based partitioning, facilitating communication between components and ensuring consistent processing and updates across the system. We often use pub-sub and reliable message queues to complement transactions in big-scale distributed systems for the following benefits. 
Decoupling: Pub-sub and message queues enable the decoupling of different components in a system, allowing producers and consumers to evolve independently. Producers can publish messages without knowing the details of the consumers, and consumers can process messages without knowing the details of the producers. This decoupling improves the maintainability and scalability of the system.
Multiple Subscribers: In a pub-sub system, multiple subscribers can consume messages from a single publisher, allowing for parallel processing and the implementation of different actions in response to a single event. This can help to build more complex and flexible systems with various processing pipelines.
Event-driven architecture: Pub-sub and message queues enable event-driven architectures, where components react to events instead of being called explicitly. This approach can lead to more modular and maintainable systems, as components can be easily added, removed, modified, or scaled without impacting the overall architecture. Message queues and pub-sub patterns facilitate asynchronous communication between components, allowing them to operate independently and concurrently. This allows for better resource utilization, improved performance, and reduced latency in the system.
Load Balancing: Reliable message queues can distribute messages evenly among multiple consumers, effectively load balancing the processing workload. This can help scale the system and handle high traffic or processing loads more efficiently
Fault Tolerance and Resilience: Message queues can store messages temporarily, providing a buffer that helps to handle failures, crashes, or temporary slowdowns in components. This improves the fault tolerance and resilience of the system, ensuring that messages are not lost and can be processed even if a component is temporarily unavailable.
By using message queues in conjunction with data partitioning and functionality-based partitioning, developers can create scalable and flexible systems that can handle diverse workloads and functionalities.
Case Study 14
How Google Ads builds on OLTP and OLAP queries? 
Goal: Learn how a major distributed data system evolved over two decades 

Google Ads is one of the world’s most successful products that makes over a hundred billion US dollars a year. It’s a platform that allows businesses to advertise their products or services on Google's search engine results pages and across the Google network. Advertisers can create ads, set budgets, and target specific keywords, locations, and demographics to optimize reaching their desired audience. The platform uses a pay-per-click (PPC) pricing model, where advertisers are charged each time someone clicks on their ad. 
Between 2000 and 2012, Google Ads grew from zero to a multi-tens of billions of dollars product. (In 2023, it’s closer to 250B$/year.) The system was designed to handle millions of queries every second. Here’s a quick overview of how it worked.  
The advertisers would use the Ads Portal to login to their accounts, and adjust keywords, budgets, and demographics. The system relied on a set of replicated MySQL engines for data storage, indexing and transactions.
When users searched on Google, keywords were sent to an AdServer (custom C++ servers) to check for relevant ads. The AdServer would check the AdShard servers, which held partitions of ad data from MySQL, to find potential matches and determine the ranking of ads. When a user clicked on an ad, that information would be appended to a LOG for later processing. Periodically, this LOG data was aggregated to produce reports for the advertiser, and to train early machine learning models to improve ad ranking. 
While this worked great for over a decade, by ~2012 the Ads team built and switched to the F1 database, a distributed relational database system. The key goals of F1's design are scalability, availability, along with consistency and usability of traditional SQL databases. F1 is built on Spanner, which provides synchronous cross-datacenter replication and strong consistency. F1 includes a fully functional distributed SQL query engine and automatic change tracking and publishing. F1 is able to achieve all these goals by making trade-offs and sacrifices, making it a hybrid of traditional relational databases and scalable key-value systems like Bigtable.
Case Study 15
How Discord stores trillions of messages? 

Goal: Learn how a major distributed data system evolved over five years

Discord is a popular communication platform used by gamers and interest-based communities. In 2023, the app is used by more than 150 million monthly active users communicating over 4 billion conversation minutes daily. 
In 2017, Discord shared its journey of storing billions of messages, and migrating its database to Apache Cassandra (from MongoDB) for scalability, fault-tolerance, and lower maintenance. Cassandra, originally developed at Facebook, is a popular open-source ‘’wide-column’’ NoSQL database. 
However, by 2022, Discord's Cassandra-based system storing trillions of messages experienced performance issues and maintenance challenges. Latency was unpredictable, and some maintenance operations became too expensive to execute. Discord migrated to ScyllaDB. ScyllaDB is a high-performance (written in C++) drop-in replacement for Cassandra, compatible with Cassandra’s APIs. Per Discord’s blog, ScyllaDB provides the same scalability and fault tolerance as Cassandra with less maintenance and improved performance.
Definitions

Recall a key-value store is a simple NoSQL database that stores data as key-value pairs, where the key is a unique identifier used to locate the associated value. The data model is straightforward and does not involve any columns, tables, or relationships.

Motivation: They are ideal for use cases that require simple data storage, caching, configuration data, or storing session information. Examples of key-value stores include Redis, Amazon DynamoDB (when used as a key-value store)

A wide-column database, also known as a column-family or columnar store, organizes data into tables with rows and columns, similar to relational databases. However, the schema is more flexible, allowing each row to have a different set of columns, and columns can be added or removed on the fly. The primary key is composed of a partition key and an optional set of clustering columns. The partition key determines which node the data is stored on, and clustering columns define the order of data within a partition.

Motivation: Wide-column databases are well-suited for handling large volumes of structured, semi-structured, or unstructured data, and they are particularly good at managing sparse data. They are often used in use cases that require fast writes and range queries. Examples include Apache Cassandra, ScyllaDB, and Google’s Bigtable.

Example Discord message store 

This sample code shows how to connect to a Cassandra or ScyllaDB instance, create a keyspace and table for a Discord-like messaging app. Note that we need a live Cassandra or ScyllaDB server running on a small cluster of machines to run this code. You can play with this code in the Distributed Systems colab.

See sample functions to store and retrieve messages. Also, an example to store a message from author_id= 1001 on channel_id=1.

In these examples, we use CQL (Cassandra Query Language), which draws inspiration from SQL.

""")
engine.runAndWait()

# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE 15 < LENGTH(Tweets.content);
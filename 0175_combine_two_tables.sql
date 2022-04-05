# https://leetcode.com/problems/combine-two-tables/

SELECT
  firstName,
  lastName,
  city,
  state
FROM
  Person a
  LEFT JOIN Address b ON a.personId = b.personId;

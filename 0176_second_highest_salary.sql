# https://leetcode.com/problems/second-highest-salary/
# https://leetcode-cn.com/problems/second-highest-salary/solution/di-er-gao-de-xin-shui-by-leetcode/

SELECT
  IFNULL(
    (
      SELECT
        DISTINCT salary
      FROM
        Employee
      ORDER BY
        salary DESC
      LIMIT
        1 OFFSET 1
    ),
    NULL
  ) AS SecondHighestSalary;

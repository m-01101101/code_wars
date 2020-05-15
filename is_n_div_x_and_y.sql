-- you can create functions that can be reused
CREATE FUNCTION isDivisible(n int, x int, y int)
RETURNS boolean AS $$
BEGIN
IF (mod(n, x) = 0 AND mod(n, y) = 0) THEN
  RETURN True;
ELSE
  RETURN False;
END IF;
END;
$$ LANGUAGE plpgsql;

SELECt id, isDivisible(n, x, y) AS res FROM kata

----------------------------

SELECT id, n % x = 0 AND n % y = 0 AS res FROM kata



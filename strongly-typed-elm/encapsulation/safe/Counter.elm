module Counter exposing (Counter, zero, increment, getCount)

type Counter = PrivateCounter Int

zero : Counter
zero = PrivateCounter 0

increment : Counter -> Counter
increment (PrivateCounter count) = PrivateCounter (count + 1)

getCount : Counter -> Int
getCount (PrivateCounter count) = count

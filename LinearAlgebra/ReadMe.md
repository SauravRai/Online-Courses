Linear Algebra contents

From 3blue1brown:
*****************
Lecture 1: Vectors and Essence of Linear Algebra
*************************************************
https://www.3blue1brown.com/lessons/vectors#interpretations-of-vectors

https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1&t=141s

Lecture 2:Linear combinations, span, and basis vectors
*************************************************
https://www.3blue1brown.com/lessons/span

https://www.youtube.com/watch?v=k7RM-ot2NWY&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=2
 
 
Lecture 3: Linear transformations and matrices
*************************************************
https://www.3blue1brown.com/lessons/linear-transformations

https://www.youtube.com/watch?v=kYB8IZa5AuE&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=3
 
Transformation is a fancy word for function. It takes input as vector and spits out output as some vector. 
So why to use the word transformation instead of function? 
To visualize the input and output relation. Moving input vector to output vector.
In Linear algebra, we restrict to just linear functions/transformations: The linear thing has two properties. 

(1) Lines remains lines 
(2) Origin remains fixed. 

In general, we can say that linear of the Grid lines remain parallel and evenly spaced so that origin remains fixed. 
Examples are shear, rotation around the center. 

Bonus point: think and visualize Matrices as Tranformations that will be the base for Linear Algebra.
 
Lecture 4: Matrix multiplication as composition -> Composition of the two separate transformations. 
*************************************************
https://www.3blue1brown.com/lessons/matrix-multiplication

https://www.youtube.com/watch?v=XkY2DOUCWMU&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=4
 
Lecture 5: Three-dimensional linear transformations
*************************************************
https://www.3blue1brown.com/lessons/3d-transformations

https://www.youtube.com/watch?v=rHLEWRxRGiM&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=5
 
Lecture 6: The determinant (think in terms of area as how much it scaled/increases/decreases, it is determined by the determinant)
*************************************************
It has magnitude which tells us as about how much it has scaled and the positive/negatives tells us about the orientation after the transformation. 

https://www.3blue1brown.com/lessons/determinant

https://www.youtube.com/watch?v=Ip3X9LOh2dk&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=6
Note: When the determinant is 0, it means the Columns must be linearly dependent as the transformed vector will be in a line :)
      Negative determinant meanning the orientation is flipped. 
      Positive determinant meaning the area is scaled by some factor.
 
Lecture 7: Inverse matrices, column space and null space
*************************************************
https://www.3blue1brown.com/lessons/inverse-matrices

https://www.youtube.com/watch?v=uQhTuRlWMxw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab

* Linear system of equations ( A X = V ) where A is the matrix/transformation that will be applied, X is the input vector and V is the output vector. 
We are looking for a vector X which after applying A (a transformation) will be Y that is the output vector. 

* Inverse matrices/Transformation 
A(inverse) x A = Transformation which does nothing (and that is Identity transformation)
If det =0, there exists no A (inverse) because we are now in a line (1 D space)
 
* Rank: No of dimensions in the output of a transformation 
Rank 1 means line and Rank 2 means a Plane, Rank 2 means 3D space.
 
* Set of all possible such outputs Av (line, plane or 3d) is called as Column space (columns tells where basis vector lands)
Column space is the span of columns or no of dimensions in the colmun space.
 
* When Rank is equal to no of columns then matrix, it is called as full rank. 
Zero vector is always present in columns space.
 
* Null space (Kernel): The space/set of vectors that lands on the origin is called as the null space. They all land in the zero/origin.




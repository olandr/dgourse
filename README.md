> **Please note**:
This whole repo got transferred from my school account. Hence the lack of commits, issues and project-boards etc.

# kthgraph
Experiments with a graph db (dgraph) focused on course relations on KTH

## Introduction
A graph db is a database as any other, with the bi-clause that it is not structured as a table. A graph database is rather structured as a mathematical graph with vertices and edges.
### Why use a graph db for this project?
One of the main benefits of using a graph db is the relational properties. E.g. If we have two vertices, o and o, related as, o->o, the relationship is obvious! Using a SQL db one would probably have to map multiple rows across multiple tables, then use `Join` to present the relationship. Very tedious (I presume) and not very clear.

Further, as this project wants to map courses onto each other, we want to show each course's relationship to other courses, we will most certainly habe an un-uniformed distribution of relationships. Meaning, certain courses will have more necessities (course requirements) than others. Thus, a table of values (a SQL db) will have many empty cells, as the course with most prerequisites defines the width of the table. This is ugly and not very readable!

### Why dgraph?
Idk, sounds like a good graph db. Might try out Cayley, Neo4j or JanusGraph too just to see the difference.

### Difficulties imply errors
Throughout this project there has been many difficulties and setbacks. These has been formulated as issues, and can thus be noted at said page. The main importance of these difficulties has been that I have battled them in various ways. Let me being by formulating the major-est difficulties:
  1. [Same name courses with different codes](https://gits-15.sys.kth.se/simonalu/kthgraph/issues/7).
  2. [Diff names, diff codes --- same struct](https://gits-15.sys.kth.se/simonalu/kthgraph/issues/8).
  3. [Non-existant courses](https://gits-15.sys.kth.se/simonalu/kthgraph/issues/12).

Some of these issues is _very_ significant in what capacity it affects the dgraph. Id est, the first (1.) is a very important issue to combat, since (as explained in the issue) the "cool graph structure" will not be present. The (2.) is in essence similar to 1., only that not as many courses is subject to this. This issue is also **alot** more difficult to fix --- as I do not know all courses that falls under this category. Regarding 3. it has to be noted that this is a major problem, but really a slight side-effect of preforming various formatting regexes. It is an annoying error and I have tried to fix it to the best of my capability. However, as this project is comming to an end I limited me to only fix these errors for the courses that I felt mattered to me --- a small subset of the CDATE courses.

### Future
The future for this project is bright. With the current formatting, it is very easy to edit, add or delete a course at any time or place. It is very easy to make interesting queries or data-objects (etc. like a node that acts as a Student taking various courses). I will for sure come back to this project at a later time. But for now, I need a break.


## Query example:
```GraphQL
{
  cs(func: eq(code@.,"compsci")) @recurse(depth:3) {
    uid
    name@.
    course
    code@se
    track
  }

  acm(func: eq(code@.,"appCompMath")) @recurse(depth:3) {
    uid
    name@.
    course
    code@se
    track
  }
}
```

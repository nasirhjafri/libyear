# libyear

A simple measure of software dependency freshness. It is a single number telling you how up-to-date your dependencies are.

## Example 1
For example, a rails 5.0.0 dependency (released June 30, 2016) is roughly 1 libyear behind the 5.1.2 version (released June 26, 2017).

## Simpler is Better
There are obviously more nuanced ways to calculate dependency freshness. The advantage of this approach is its simplicity. You will be able to explain this calculation to your colleagues in about 30s.

## Example 2
If your system has two dependencies, the first one year old, the second three, then your system is four libyears out-of-date.

## A Healthy App
At Singlebrook we try to keep our client’s apps below 10 libyears. We regularly rescue projects that are over 100 libyears behind.


## Etymology
"lib" is short for "library", the most common form of dependency.

## References
J. Cox, E. Bouwers, M. van Eekelen and J. Visser, Measuring Dependency Freshness in Software Systems. In Proceedings of the 37th International Conference on Software Engineering (ICSE 2015), May 2015 https://ericbouwers.github.io/papers/icse15.pdf

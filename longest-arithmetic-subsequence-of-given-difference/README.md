<h2><a href="https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference">Longest Arithmetic Subsequence of Given Difference</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<p>1.8K</p>
<p>52</p>
<p>Companies</p>
<hr>
<p>Given an integer array <code>arr</code> and an integer <code>difference</code>, return the length of the longest subsequence in <code>arr</code> which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals <code>difference</code>.</p>

<p>A subsequence is a sequence that can be derived from <code>arr</code> by deleting some or no elements without changing the order of the remaining elements.</p>

<p> </p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4], difference = 1
<strong>Output:</strong> 4
<strong>Explanation: </strong> The longest arithmetic subsequence is [1,2,3,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,5,7], difference = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong> The longest arithmetic subsequence is any single element.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,5,7,8,5,3,4,2,1], difference = -2
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest arithmetic subsequence is [7,5,3,1].
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= arr.length <= 10^5</code></li>
	<li><code>-10^4 <= arr[i], difference <= 10^4</code></li>
</ul>

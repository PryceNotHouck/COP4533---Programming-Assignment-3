Pryce Houck (57790944)
Trevor DeBord (40228131)

Question 2:
Define $OPT(i, j)$ as the highest value common subsequence between 
$\{a_1, a_2, \dots, a_i \} \subseteq A$ and 
$\{b_1, b_2, \dots, b_j \} \subseteq B$.

At each iteration, one of the following holds:

- **Case 1:** $a_i = b_j$  
  $\rightarrow$ This value is in the HVLCS, so add $v_{a_i}$ and recurse onto the next elements in either array:  
  $$OPT(i, j) = v_{a_i} + OPT(i - 1, j - 1).$$

- **Case 2:** $a_i \neq b_j$  
  $\rightarrow$ This value is not in the HVLCS, so take the maximum of excluding either element:  
  $$OPT(i, j) = \max\{OPT(i, j-1), OPT(i-1, j)\}.$$

- **Base Cases:**  
  $$OPT(i, 0) = 0, \quad OPT(0, j) = 0$$  
  because the maximum matching subsequence has value 0.

$$
OPT(i, j) =
\begin{cases}
0 & \text{if } i = 0 \text{ or } j = 0 \\
\max\{OPT(i - 1, j),\; OPT(i, j-1)\} & \text{if } a_i \neq b_j \\
v_{a_i} + OPT(i - 1, j - 1) & \text{if } a_i = b_j
\end{cases}
$$


Question 3:
Time complexity analysis of HVLCS A and B
psuedocode:
    helper func:
    //runtime is O(n) for find(curr), where n = length of subsequence
    def is_common(deq, sequence):
        subsequence = sequence
        while len(deq) != 0:
            curr deq.popleft()
            found = subsequence.find(curr)
            if found != -1:
                subsequence = subsequence[found:]
            else:
                return False
        return True

    def max_subseq(char dict, seq list):
        str A
        str B
        A_subseq = set()
        B_subseq = set()

        //creates subsequences for A
        //O(A^2), iterating through each value in the string and creating substrings
        //string slicing takes O(N) as it creates new strings        
        //~O(A^3)
        for i < len(A):
            j = i+1
            while j <= len(A):
                A_subseq.add(A[i:j])
                j+=1

        //creates subsequences for B
        //O(B^2), iterating through each value in the string and creating substrings
        //string slicing takes O(N) as it creates new strings
        //~O(B^3)
        for i < len(B):
            j = i+1
            while j <= len(B):
                B_subseq.add(B[i:j])
                j+=1

        //sorts A and B list of subsequence
        //O(2NlogN) sorting for both
        A_subseq = sorted(list(A_subseq))
        B_subseq = sorted(list(B_subseq))

        //if sub matches in A_subseq and B_subseq, make a comparison
        //O(2P+2PlogP) where P = len of A_subseq / B_subeq (combining both sub in X_subseq codeblocks)
        //trivially small operations when compared to A and B string length
        for sub in A_subseq:
            val = 0
            for i in sub:
                val += char[i]

            if sub in B_subseq:
                common[sub] = val
                continue

            sub_split = deque(sub)
            if is_common(sub_split, B):
                common[sub] = val


        for sub in B_subseq:
            val = 0
            for i in sub:
                val += char[i]

            if sub in A_subseq:
                common[sub] = val
                continue

            sub_split = deque(sub)
            if is_common(sub_split, A):
                common[sub] = val

        //O(1)
        max_val = max(common.vals())
        max_sequence = [key for key, val in common.items() if val == max_val][0]

        return max_val, max_sequence

runtime: O(n + A^3 + B^3 + 2nlogn +2p + 2plogp + 1) simplies to O(A^3)



Assumptions:
It is assumed that there will never be a request for strings of size <= 2

Usage Instructions: 
adjust the "input_sizes" list within main.py to adjust the size of strings to evaluate.

Dependencies:
main.py requires the environment to include the matplotlib and numpy libraries, can be installed through pip or conda in terminal.

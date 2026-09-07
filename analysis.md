# Security Analysis of Repeating-Key XOR
### Author: William Disman

## 1. Correctness
Let $m = m_0, m_1, ... \space m_{n-1} \in \mathbb{B}^*$ and $k = k_0, k_1, ... \space k_{\ell-1} \in \mathbb{B}^+$. Given $\ell > 0$ (the length of the key is greater than zero), $i \bmod \ell$ is defined for all values where $i \geq 0$. $\mathsf{Enc}_k(m)_i = c_i = m_i \oplus k_{i \bmod \ell}$ for $0 \leq i \lt n$, and $\mathsf{Dec}_k(c)_i = c_i \oplus k_{i \bmod \ell}$.

Thus, for each index $i$:

$$
\mathsf{Dec}_k(\mathsf{Enc}_k(m))_i = c_i \oplus k_{i \bmod \ell} = (m_i \oplus k_{i \bmod \ell}) \oplus k_{i \bmod \ell}
$$

The associative property of $\oplus$ states that $(a \oplus b) \oplus c = a \oplus (b \oplus c)$. Additionally, $x \oplus x = 0$ and $x \oplus 0 = x$. Therefore, $(m_i \oplus k_{i \bmod \ell}) \oplus k_{i \bmod \ell} = m_i \oplus (k_{i \bmod \ell} \oplus k_{i \bmod \ell}) = m_i \oplus 0 = m_i.$ Given the length of $c$ always equals the length of $m$ and the above calculations are true for every $i$, $\mathsf{Dec}_k(\mathsf{Enc}_k(m)) = m$ for all values of $m$ and all values of $k$ where $\ell > 0$. An empty message where $n = 0$ falls within the parameters of the above calculations, meaning both $\mathsf{Dec}_k$ and $\mathsf{Enc}_k$ will return empty strings.

## 2. Known Plaintext
Assuming an attacker knows a matched pair $(m_i, \space c_i)$ at position $i$ and the algorithm on which a repeating-key XOR is built, they can determine exactly one byte of the key. Since $c_i = m_i \oplus k_{i \bmod \ell}$, XOR-ing both sides by $m_i$ results in $c_i \oplus m_i = k_{i \bmod \ell}$. Thus, with the information the attacker has they learn exactly one byte of the key. However, since the key repeats, every $\ell ^{\text{th}}$ index of $m$ is encrypted with the same $k_i$. Using brute-force methods, the attacker can attempt to find the length of the key, $\ell$, and determine every character $m_j$ where $j = i \bmod \ell$.

## 3. Key Reuse
If equal length messages $m$ and $m'$ are encrypted with the same key, $c_i = m_i \oplus k_{i \bmod \ell}$ and $c_i' = m_i' \oplus k_{i \bmod \ell}$, XOR-ing the two ciphertexts will result in the value of the two messages being XOR-ed, bypassing the need to know the key. For each index $i$:

$$
c_i \oplus c_i' = (m_i \oplus k_{i \bmod \ell}) \oplus (m_i' \oplus k_{i \bmod \ell}) = m_i \oplus m_i'
$$

Because of the associative and commutative properties of $\oplus$, the two copies of $k_{i \bmod \ell}$ cancel out. The attacker can learned the bitwise difference between $m$ and $m'$ without knowing any information about $k$. In any case where $m_i \oplus m_i' = 0$, the plaintext of $m_i$ is equal to the plaintext of $m_i'$. Although this information is immediately clear to an attacker, what is not immediately clear is what the plaintext of $m$ or $m'$ is. The attacker would need to utilize language statistics (the frequency at which specific letters appear in a given language) and additional brute-force in order to gain access the *possible* plaintext values.

## 4. One-Time Pad Comparison
A one-time pad requires the key to be (at least) the same length as the message so that no index is reused. Additionally, the key bytes should be chosen uniformly at random and each key should only be used once. The same key (or parts of it) should not be used for messages of the same or lesser length. Finally, in order for a one-time pad to be effective, each party must have access to the key before it is used. For example, each party may have a book of key values and start from the same index in the book. 

A repeating-key XOR violates the length condition when $\ell \lt n$. The same byte of the key must be used more than once since the message is longer than the key. This introduces insecurities like those explored in section 2. Additionally, a repeating-key XOR may encrypt multiple messages using the same key. This is not permitted with a one-time pad. Reusing the same key can introduce vulnerabilities like those described in section 3. Depending on the implementation, uniformity and key-distribution conditions may be violated as well, but this is not inherently the case for all repeating-key XOR implementations.

## 5. Security Limits
A short repeating key is less effective given the analysis in section 2. If an attacker uses prior knowledge of the byte-distributions of natural-language English text, the attacker can use brute-force attacks as detailed in Lecture 2. With a shorter key, the number of times the key is repeated is increased. For example, a 2 byte key encrypting a 32 byte message means that the same byte is used 16 times. Thus, a single known plaintext byte automatically reveals every other word in plaintext. If a key is repeated more than a few times, the confidentiality of the ciphertext begins to reduce exponentially. Thus, a repeating-key XOR where $n \gg \ell$ loses confidentiality.

On the other hand, a uniformly random key at least as long as the message and never reused can provide more confidentiality. Similar to a one-time pad, the ciphertext is statistically independent of the plaintext. The probability $C = c \space | \space M = m$ is uniform for all values of $m$. By definition, perfect secrecy is obtained.

Despite achieving perfect secrecy, the integrity of the message cannot be guaranteed. If an attacker intercepts and manipulates the ciphertext, there is no way for the recipient to verify that the ciphertext was not tampered with. Perfect secrecy does not guarantee that a message is authentic. Additionally, the two parties must have a secure way to distribute the key. If the length of the key is just as long as the message, the total amount of information that needs to be communicated between the two parties is doubled.

## References

Xu, Lei. "Lecture 2: Vigenere Cipher and Cryptoanalysis" 29 Aug. 2026, CS-47221, Introduction to Cryptography, Kent State University. PDF download. 

Xu, Lei. "Lecture 3: Security Definitions and Perfect Secrecy" 4 Sept. 2026, CS-47221, Introduction to Cryptography, Kent State University. PDF download.

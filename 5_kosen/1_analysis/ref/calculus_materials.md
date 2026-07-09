# #1①：[復習] 微分法
演習書「解法演習 微分積分I」p.24 - 49

［目標］今考えているものが「変数単体($x$など)」なのか「定数」なのか「変数部分」なのかを適切に判断し，脳内で線形性を組み立てて素早く微分することができるようになる．代数関数，初等超越関数の微分をマスターする．

## 定理 1.1 微分の演算
以下，$f$と$g$は$x$の関数，$\lambda,~\mu$は任意のスカラーとし，プライム（$^{\prime}$）は$x$による微分を表すこととする．
[1] $(\lambda f\pm \mu g)'=\lambda f'\pm \mu g'.$ (線形性)
[2] $(f\cdot g)'=f'g+fg'.$ (乗法, 積)
[3] $(f/g)'=\left(f'g-fg'\right)/g^{2}.$ (除法, 商)

## 定理 1.2 微分公式
[1] $\left(x^{n}\right)'=nx^{n-1}.$ (冪乗)
[2] $\left(c\right)'=0,~c=\mathrm{const}.$ (定数微分)
[3] $y=f(x)$を$u=g(x)$で置換$\rightarrow$ $\displaystyle\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}.$ (合成関数)
[4] $y=f^{-1}(x)$の微分$\rightarrow$ $\displaystyle\frac{dy}{dx}=\frac{1}{\frac{dx}{dy}}.$ (逆関数)
[5] $[\{f(x)\}^{n}]^{\prime}=n\cdot\{f(x)\}^{n-1}\cdot f'(x)$. (累乗微分)
[6] $(\sin x)'=\cos x,~(\cos x)'=-\sin x,~(\tan x)'=(\cos^{2}x)^{-1}$. (三角関数)
[7] $(\sin^{-1}x)'=\frac{1}{\sqrt{1-x^{2}}},~(\cos^{-1}x)'=\frac{-1}{\sqrt{1-x^{2}}},~(\tan^{-1}x)'=\frac{1}{1+x^{2}}$. (逆三角関数)
[8] $(\log|x|)'=\frac{1}{x},~(e^{x})'=e^{x},~(a^{x})'=a^{x}\log a.$ (指数/対数関数)

**問1** 関数$y=x^{5}-2x^{3}+x+3$を微分する過程について，以下の問いに答えよ．(例題45(1))

(1) 関数$y$のそれぞれの項について，「定数部分」と「変数部分」をそれぞれ分けて表を埋めよ．また，変数部分を$x$で微分したものをその右にかけ．

| 項 | 定数部分($\lambda$) | 変数部分($f(x)$) | 導関数($f'(x)$) |
|---|---|---|---|
| 第1項 | 1 | $x^5$ | $5x^4$ |
| 第2項 | -2 | $x^3$ | $3x^2$ |
| 第3項 | 1 | $x$ | $1$ |
| 第4項 | 3 | - | $0$ |

(2) 第$n$項の定数部分を$\lambda_{n}$，変数部分を$f_{n}(x)$，導関数を$f_{n}^{\prime}(x)$とすると，$y$は次のように展開できる．
$$ y=\lambda_{1}f_{1}(x)+\lambda_{2}f_{2}(x)+\lambda_{3}f_{3}(x)+\lambda_{4}f_{4}(x). $$
定理1.1 [1]の線形性を用いてこれを微分すると（つまり，$\lambda$はそのまま，$f$だけを微分する），
$$ y'=\lambda_{1}f_{1}^{\prime}(x)+\lambda_{2}f_{2}^{\prime}(x)+\lambda_{3}f_{3}^{\prime}(x)+\lambda_{4}f_{4}^{\prime}(x). $$
さて，(1)で求めた式を上式に代入することで，$y$を微分せよ．
$$ y'=1\cdot 5x^{4}-2\cdot3x^{2}+1\cdot1+3\cdot0=5x^{4}-6x^{2}+1. $$

**問2** 関数$y=(x^{2}+x+1)^{4}$を微分する過程について，以下の問いに答えよ．(例題47(1))

(1) 定理1.2の微分公式[5]を用いたい．この時，$f(x)$と$n$はそれぞれ，$f(x)=x^{2}+x+1,~n=4$とすれば良い．
(2) 上で定めた$f(x)$を微分すると，$f'(x)=2x+1$となる．
(3) 公式を適用し，関数$y=(x^{2}+x+1)^{4}$を微分すると，
$$ y'=n\cdot\{f(x)\}^{n-1}\cdot f'(x)=4(x^{2}+x+1)^{3}\cdot(2x+1). $$

**問3** 関数$y=\sin(2x+2)$を微分する過程について，以下の問いに答えよ．(例題49(1))

(1) $\sin$の微分には，定理1.2の公式[6]を用いたい．$y=\sin u$とするためには，$u=2x+2$とすれば良い．
(2) 定理1.2の公式[3]において，$\frac{dy}{du}$は「$y=\sin u$を$u$で微分」という意味である．よって，三角関数の微分公式より，$\frac{dy}{du}=(\sin u)'=\cos u$．
(3) 定理1.2の公式[3]において，$\frac{du}{dx}$は「$u=2x+2$を$x$で微分」という意味である．よって，$\frac{du}{dx}=(2x+2)'=2$．
(4) (2)と(3)で得た$\frac{dy}{du},~\frac{du}{dx}$を掛け合わせることにより，求めたい関数の導関数$y'=\frac{dy}{dx}$を求めよ．
$$ y'=\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}=\cos u\cdot 2=2\cos(2x+2). $$
(5) [発展] $\sin$の引数が$2x+2$でなくて，一般的な関数であったとき，すなわち$y=\sin(f(x))$であった時，同様にして導関数$y'$を求めよ．（解答欄略）

### 実践問題

**Q1.** 次に示す$y$を微分せよ．
(1) $y=(5x^{2}+4x+9)^{3}$ [累乗微分] Ans: $y'=6(5x^{2}+4x+9)^{2}(5x+2)$.
(2) $y=(4x+5)(3x+1)$ [積の微分] Ans: $y'=24x+19$.
(3) $y=(\log|4x+6|)^{4}$ [合成関数，累乗微分] Ans: $y'=8(\log|4x+6|)^{3}(2x+3)^{-1}$.
(4) $y=\sin^{-1}(9x+2)$ [逆三角関数] Ans: $y'=3\sqrt{3}(-27x^{2}-6x-1)^{-1/2}$.
(5) $y=e^{ax+b},~~(a,b=\mathrm{const}.)$ [合成関数，指数関数] Ans: $y'=ae^{ax+b}$.
(6) $y=[\tan(2x+4)]^{2}$ [合成関数，累乗微分，三角関数] Ans: $y'=4\tan(2x+4)[\cos^{2}(2x+4)]^{-1}$.

**Q2.** [発展] 次の公式を導出せよ．
(1) $(\sin^{-1}x)'=\frac{1}{\sqrt{1-x^{2}}}$
(2) $(\cos^{-1}x)'=\frac{-1}{\sqrt{1-x^{2}}}$
(3) $(\tan^{-1}x)'=\frac{1}{1+x^{2}}$

---

# #1②：$n$次導関数(高階導関数)
演習書「解法演習 微分積分I」p.54 - 55
「大学1・2年生のためのすぐわかる微分積分」p.63 - 65

［目標］さまざまな関数の高階導関数の挙動を理解し，任意の自然数$n$に対する$n$次導関数を求められるようになる．

## 定理 要素として使える数列
[1] $\{a_{n}\}_{n=1}^{\infty}=\{-1,1,-1,1,\ldots\},~\text{一般項}~a_{n}=(-1)^{n}.$
[2] $\{a_{n}\}_{n=1}^{\infty}=\{1,-1,1,-1,\ldots\},~\text{一般項}~a_{n}=(-1)^{n+1}~~\text{or}~~(-1)^{n-1}.$
[3] $\{a_{n}\}_{n=1}^{\infty}=\{k,k^{2},k^{3},\ldots\},~\text{一般項}~a_{n}=k^{n}.$
[4] $\{a_{n}\}_{n=0}^{\infty}=\{1,1,2,6,\ldots\},~\text{一般項}~a_{n}=n!.$
[5] $\{a_{n}\}_{n=0}^{\infty}=\{\sin k,\cos k,-\sin k, -\cos k, \sin k,\ldots\},$
一般項 $a_{n}=\sin\left(k+\frac{n\pi}{2}\right)=\sin k\cos\frac{n\pi}{2}+\cos k\sin\frac{n\pi}{2}.$

**問1** [簡単な$n$次導関数] $y=\sin x$の$n$次導関数$y^{(n)}$を求める過程について，以下の問いに答えよ．(例題60(2))

(1) $y$を一階微分せよ．
$$ y'=(\sin x)'=\cos x. $$
(2) $y$を二階微分せよ（二階微分とは，$y^{\prime}$をさらに微分するということ）．
$$ y^{\prime\prime}=(y')^{\prime}=(\cos x)'=-\sin x. $$
(3) $y$を三階微分せよ．
$$ y^{\prime\prime\prime}=(y^{\prime\prime})^{\prime}=(-\sin x)^{\prime}=-\cos x. $$
(4) $y$の四階導関数まで求めて，以下の表を埋めよ．また，これらの周期性に合う数列を，定理から選んで記号をかけ．

| $n$ | $n$階導関数$y^{(n)}$ |
|---|---|
| 1 | $y'=\cos x$ |
| 2 | $y^{\prime\prime}=-\sin x$ |
| 3 | $y^{\prime\prime\prime}=-\cos x$ |
| 4 | $y^{(4)}=\sin x$ |

要素として使える数列：[5]．

(5) (4)で選んだ要素（数列）を用いて，$n$次導関数$y^{(n)}$を式で表せ．
$$ y^{(n)}=\sin\left(k+\frac{n\pi}{2}\right). $$

**問2** [組み合わせ] $y=x^{\alpha}~(\alpha\in\mathbb{R})$の$n$次導関数$y^{(n)}$を求める過程について，以下の問いに答えよ．

(1) $y$を一階微分せよ．
$$ y'=(x^{\alpha})'=\alpha x^{\alpha-1}. $$
(2) $y$を二階微分せよ．
$$ y^{\prime\prime}=(y')^{\prime}=(\alpha x^{\alpha-1})^{\prime}=\alpha(\alpha-1)x^{\alpha-2}. $$
(3) $y$を三階微分せよ．
$$ y^{\prime\prime\prime}=(y^{\prime\prime})^{\prime}=(\alpha(\alpha-1)x^{\alpha-2})^{\prime}=\alpha(\alpha-1)(\alpha-2)x^{\alpha-3}. $$
(4) $y$の三階導関数までをまとめ，以下の表を埋めよ．

| $n$ | $n$階導関数$y^{(n)}$ |
|---|---|
| 1 | $y'=\alpha x^{\alpha-1}$ |
| 2 | $y^{\prime\prime}=\alpha(\alpha-1)x^{\alpha-2}$ |
| 3 | $y^{\prime\prime\prime}=\alpha(\alpha-1)(\alpha-2)x^{\alpha-3}$ |

(5) ところで，階乗と順列には次のような性質がある．
$$ {}_{r}\mathrm{P}_{n}=\frac{r!}{(r-n)!}=r(r-1)(r-2)\cdots(r-n+1). $$
この性質を用いて，$n\leq\alpha$のときと$n>\alpha$における$n$次導関数$y^{(n)}$をそれぞれ式で表せ．
$$ y^{(n)}={}_{\alpha}\mathrm{P}_{n}\cdot x^{\alpha-n}~(n\leq\alpha),~~y^{(n)}=0~(n>\alpha). $$

**問3** [数学的帰納法による証明] 前問で導出した$y=x^{\alpha}$の$n$次導関数$y^{(n)}$が，求めた式であることを数学的帰納法を用いて証明したい．以下の問に答えよ．

(1) 数学的帰納法を用いて証明するとき，次の二つが成り立つことを示せば良い．穴を埋めよ．
[i] $n=1$のとき$y^{(n)}={}_{\alpha}\mathrm{P}_{n}\cdot x^{\alpha-n}$が成り立つ．
[ii] 任意の自然数$k$に対して，$n=k$のとき$y^{(k)}={}_{\alpha}\mathrm{P}_{k}\cdot x^{\alpha-k}$が成り立つと仮定したとき，$n=k+1$のとき$y^{(k+1)}={}_{\alpha}\mathrm{P}_{k+1}\cdot x^{\alpha-(k+1)}$が成り立つ．
(2) 前問で求めた式に$n=1$を代入して，$n=1$のときこの命題が成り立つことを示せ．
$$ y^{(1)}=y'={}_{\alpha}\mathrm{P}_{1}x^{\alpha-1}=\alpha x^{\alpha-1}. $$
(3) 前問で求めた式に$n=k+1$を代入して，$n=k$が成り立つ仮定の下で$n=k+1$のときこの命題が成り立つことを示せ．
$$ y^{(k+1)}=\left(y^{(k)}\right)'=({}_{\alpha}\mathrm{P}_{k}\cdot x^{\alpha-k})^{\prime}={}_{\alpha}\mathrm{P}_{k}\cdot(\alpha-k)x^{\alpha-k-1}={}_{\alpha}\mathrm{P}_{k+1}\cdot x^{\alpha-(k+1)}=(\mathrm{R}). $$

---

# #1③：三角関数の合成

［目標］三角関数の合成に関する考えを理解し，色々な三角関数を合成できるようになる．

## 定理 三角関数の合成
正弦函数$y_{1}=a\sin x$と余弦函数$y_{2}=b\cos x$の和$y$は，以下のような1つの正弦函数で表すことができる．
$$ y=y_{1}+y_{2}=a\sin x+b\cos x=\sqrt{a^{2}+b^{2}}\sin(x+\alpha)~~\left({}^{\exists}\alpha\in\mathbb{R}\text{ s.t. }\begin{cases}a=\sqrt{a^{2}+b^{2}}\cos\alpha\\ b=\sqrt{a^{2}+b^{2}}\sin\alpha\end{cases}\right). $$

Prf.) 実空間における話を複素空間における話に拡張し，Eulerの公式による展開を用いる．今，$\dot{z},\dot{w}\in\mathbb{C}$とし，$\dot{z}=ae^{jx},~\dot{w}=be^{i(x+\frac{\pi}{2})}$とおくと，それらの和$\dot{z}+\dot{w}$は，
$$
\begin{align*}
	\dot{z}+\dot{w}&=a(\cos x+i\sin x)+b\left[\cos(x+\frac{\pi}{2})+i\cos(x+\frac{\pi}{2})\right]\\
	&=a(\cos x+i\sin x)+b(-\sin x+i\cos x)\\
	&=a\cos x-b\sin x+i(a\sin x+b\cos x).
\end{align*}
$$

最後の式に示した下線部が，定理における$y$となっているので，$y=\Im(\dot{z}+\dot{w})$ であることがわかる．ここで，$\dot{z}+\dot{w}$を極表示するために，
$$ \dot{z}+\dot{w}=Ae^{i(x+\alpha)}=A\left[\cos(x+\alpha)+i\sin(x+\alpha)\right] $$ 
とおくと，$\dot{z}+\dot{w}$の大きさ$A$は，
$$
\begin{align*}
	A=|\dot{z}+\dot{w}|&=\sqrt{(a\cos x-b\sin x)^{2}+(a\sin x+b\cos x)^{2}}\\
	&=\sqrt{a^{2}\cos^{2}x-2ab\cos x\sin x+b^{2}\sin^{2}x+a^{2}\sin^{2} x+2ab\sin x\cos x+b^{2}\cos^{2}x}\\
	&=\sqrt{a^{2}(\cos^{2}x+\sin^{2}x)+b^{2}(\sin^{2}x+\cos^{2}x)}=\sqrt{a^{2}+b^{2}}.
\end{align*}
$$

これにより，
$$ y=\Im(\dot{z}+\dot{w})=A\sin(\theta+\alpha)=\sqrt{a^{2}+b^{2}}\sin(\theta+\alpha) $$ となるので，題意に伴う．

### 実践問題

**Q1.** 次に示す三角関数$y_{1}$と$y_{2}$を合成して，1つの正弦函数として表せ．
(1) $y_{1}=\sin x,~y_{2}=-\cos x$ [基礎数学でやった] $y=\sqrt{2}\sin\left(x-\frac{\pi}{4}\right)$.
(2) $y_{1}=10\cos\theta,~y_{2}=5\sin\theta$ [解析で扱った] $y=5\sqrt{5}\sin(\theta+\sin^{-1}\frac{2}{\sqrt{5}})$.
(3) $y_{1}=A_{1}\sin(\omega t+\phi_{1}),~y_{2}=A_{2}\sin(\omega t+\phi_{2})$ [単振動の重ね合わせ] $y=A\sin(\omega t+\phi)$.
ただし
$$ \begin{cases} A=\sqrt{(A_{1}\cos\phi_{1}+A_{2}\cos\phi_{2})^{2}+(A_{1}\sin\phi_{1}+A_{2}\sin\phi_{2})^{2}} \\ \phi=\tan^{-1}\frac{A_{1}\sin\phi_{1}+A_{2}\sin\phi_{2}}{A_{1}\cos\phi_{1}+A_{2}\cos\phi_{2}} \end{cases} $$
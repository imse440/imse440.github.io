#############
Lecture notes
#############

..
    .. include:: intro-simple-linear-reg.rst

Introduction to linear regression
=================================



.. code-block:: python
    
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('./data/advertising.csv')
    plt.scatter(x='TV', y='sales', data=df)


.. image:: images/lectures/tv_sales.png
  :width: 800
  :alt: advertising data


Questions that we may ask

- Is there a relationship between advertising budget (TV, radio, and newspaper) and the sales?
- If yes, how *strong* is the relationship?
- Is the relationship *linear*?
- How *accurately* can we estimate the effect of each channel on sales?
- Given the budget, how accurately can we *predict* future sales?
- Is there any *synergy* among the media?

`Linear regression <https://en.wikipedia.org/wiki/Linear_regression>`__
: Study the relationship between two or more variables.

.. math:: \text{sales} = f(\text{TV}) = a + b \cdot \text{TV}

`Simple linear regression <https://en.wikipedia.org/wiki/Simple_linear_regression>`__
: The model takes the form

.. math:: Y= \beta_0 + \beta_1 \cdot x + \epsilon

where

- :math:`x`: a given input to the model
- :math:`\epsilon`: the error term modeled as a `normally-distributed <https://probstats.org/normal.html>`__ random variable :math:`\epsilon \sim \text{N}(0, \sigma^2)`
- :math:`\beta_0 \text{ and } \beta_1`: unknown parameters in the model


Question: Is :math:`Y` a random variable?

- What is the expected value of :math:`Y`?
- What is the variance of :math:`Y`?
- What distribution does :math:`Y` follow?

.. math:: Y \sim \text{N}(\beta_0 + \beta_1 x, \sigma^2)


- :math:`\beta_0`: the *intercept*, the expected value of :math:`Y` when :math:`x=0`.
- :math:`\beta_1`: the *slope*, the expected change of :math:`Y` per unit change of :math:`x`.


.. Visualize :math:`\beta_0` and :math:`\beta_1`


.. .center[![:scale 65%](images/xyplane.jpg)]

Parameter estimation
====================

The problem
^^^^^^^^^^^

.. math:: \text{E}[\text{sales}] = \beta_0 + \beta_1 \cdot \text{TV}

.. .center[![:scale 85%](images/tv_sales.png)]

What would be our "best" estimates of :math:`\beta_0` and :math:`\beta_1`?
In other words, what it the model that fits the data the best?

Naturally, we may want to take a look at the "errors" that the model made in its responses (:math:`\hat{y}_i`) when compared with the actual data (:math:`y_i`) at each of the given input values :math:`x_i`.

.. .center[![:scale 60%](images/xyplane.jpg)]

.. math:: e_i=y_i-\hat{y}_i=y_i-(\beta_0+\beta_1x_i), \; i=1, 2, \cdots, n.

In statistics, these "errors" are often called "residuals", as they are the *remaining* variations in the data (:math:`y_i`) that can not be explained by a statistical model.


Question: Can we use the *sum of all the residuals* as a metric to find the best model?

.. math:: e_1+e_2+\cdots+e_n

It is not a good idea, as the positive and negative residuals would cancel each other out. 

Instead, we square the residuals before summing them up. 
The result is called the `Residual Sum of Squares (RSS) <https://en.wikipedia.org/wiki/Residual_sum_of_squares>`__.

.. math:: 

    \begin{aligned}
    \text{RSS}&=e_1^2+e_2^2+\cdots+e_n^2 \\
    \\
    &=\sum_{i=1}^n e_i^2 \\
    \\
    &=\sum_{i=1}^n \big[y_i-(\beta_0+\beta_1 x_i)\big]^2 \\
    \end{aligned}



Ordinary Least Squares (OLS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given :math:`n` pairs of data

.. math:: (x_1, y_1), (x_2, y_2), \cdots, (x_n, y_n)

We choose :math:`\beta_0` and :math:`\beta_1` such that the RSS is minimized. 

.. math:: \min_{\beta_0, \beta_1} \bigg\{ f(\beta_0, \beta_1)=\text{RSS}= \sum_{i=1}^n \big[y_i - (\beta_0 + \beta_1 x_i)\big]^2 \bigg\}

This method is called `Ordinary Least Squares (OLS) <https://en.wikipedia.org/wiki/Ordinary_least_squares>`__.



To find the minimum of the function :math:`f(\beta_0, \beta_1)`, we take partial derivatives of the function w.r.t. :math:`\beta_0` and :math:`\beta_1`, and set the derivatives to 0.

.. math:: 

    \begin{align}
    \frac{\partial f(\beta_0, \beta_1)}{\partial \beta_0} &= \sum2\big[y_i - (\beta_0 + \beta_1x_i)\big](-1)=0  \label{a}   \tag{1}\\
    \\
    \frac{\partial f(\beta_0, \beta_1)}{\partial \beta_1} &= \sum2\big[y_i - (\beta_0 + \beta_1x_i)\big](-x_i)=0 \label{b}  \tag{2}\\
    \end{align}


Then we can use linear algebra to solve for :math:`\beta_0` and :math:`\beta_1`.

From Eq. (:math:`\ref{a}`)

.. math::

    \begin{align}
    \sum y_i -\sum \hat{\beta}_0 - \sum \hat{\beta}_1 x_i &= 0 \\
    \\
    \sum y_i - n \hat{\beta}_0 - \hat{\beta}_1 \sum x_i &= 0 \\
    \\
    n \hat{\beta}_0 + \big(\sum x_i \big) \hat{\beta}_1  &= \sum y_i \label{c}  \tag{3}\\
    \end{align}


From Eq. (:math:`\ref{b}`)

.. math::

    \begin{align}
    \sum \big(x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2 \big) &= 0 \\
    \\
    \sum x_i y_i - \hat{\beta}_0 \sum x_i - \hat{\beta}_1 \sum x_i^2 &= 0 \\
    \\
    \big(\sum x_i \big) \hat{\beta}_0 + \big(\sum x_i^2 \big) \hat{\beta}_1  &= \sum x_i y_i \label{d}  \tag{4}\\
    \end{align}

Now multiply both sides of Eq. (:math:`\ref{c}`) by :math:`\sum x_i`, and multiply both sides of Eq. (:math:`\ref{d}`) by :math:`n`, we have

.. math::

    \begin{align}
    n \big(\sum x_i \big) \hat{\beta}_0 + \big(\sum x_i \big)^2 \hat{\beta}_1  &= \sum x_i \sum y_i \label{e}  \tag{5}\\
    \\
    n \big(\sum x_i \big) \hat{\beta}_0 + n \big(\sum x_i^2 \big) \hat{\beta}_1 &= n \sum x_i y_i  \label{f}  \tag{6}\\
    \end{align}

Lastly, Subtract both sides of Eq. (:math:`\ref{e}`) from Eq. (:math:`\ref{f}`), we have

.. math::

    \begin{align}
    \bigg[n \sum x_i^2 - \big(\sum x_i \big)^2 \bigg] \hat{\beta}_1 &= n \sum x_i y_i - \sum x_i \sum y_i \\
    \\
    \hat{\beta}_1 &= \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - \big(\sum x_i \big)^2} \\
    \end{align}


The intercept estimate :math:`\hat{\beta}_0` can be obtained from Eq. (:math:`\ref{c}`)

.. math::

    \hat{\beta}_0 = \frac{\sum y_i - \big(\sum x_i \big) \cdot \hat{\beta}_1}{n} = \frac{\sum y_i}{n} - \frac{\sum x_i}{n} \cdot \hat{\beta}_1 = \bar{y} - \bar{x} \cdot \hat{\beta}_1

where :math:`\bar{x}` and :math:`\bar{y}` are the sample means for :math:`x` and :math:`y` from the data. 


.. Calculus refresher
.. ^^^^^^^^^^^^^^^^^^

.. .. math:: 

..     \begin{aligned}
..     \frac{d}{dx}(c)&=0 \\
..     \\
..     \frac{d}{dx}(kx)&=k \\
..     \\
..     \frac{d}{dx}\big(x^2\big)&=2x
..     \end{aligned}


.. The chain rule:

.. .. math:: \frac{d}{dx}\bigg(f\big(g(x)\big)\bigg)=f'\big(g(x)\big)\cdot g'(x)


.. admonition:: OLS solution

    Given :math:`n` pairs of data :math:`(x_1, y_1), (x_2, y_2), \cdots, (x_n, y_n)`, the Ordinary Least Squares solution is

    .. math:: 

        \begin{aligned}
        \hat{\beta}_1 &=\frac{n\sum{x_i y_i}-\sum{x_i}\sum{y_i}}{n\sum{x_i^2}-(\sum{x_i})^2} =\frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{\sum{(x_i-\bar{x})^2}} =\frac{S_{xy}}{S_{xx}}
        \\
        \\
        \hat{\beta}_0&=\bar{y}-\bar{x}\hat{\beta}_1 \\
        \end{aligned}


Some intuition

`Sample covariance <https://en.wikipedia.org/wiki/Covariance#Calculating_the_sample_covariance>`__

.. math:: \text{cov}(x, y)=\frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{n-1}

`Sample variance <https://imse317.github.io/lectures/chap-1/measure-of-variability>`__

.. math:: \text{var}(x)=\text{cov}(x, x)=\frac{\sum{(x_i-\bar{x})^2}}{n-1}

OLS slope estimate

.. math:: \hat{\beta}_1 = \frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{\sum{(x_i-\bar{x})(x_i-\bar{x})}} =\frac{\text{cov}(x, y)}{\text{cov}(x, x)}

Roughly speaking, :math:`\hat{\beta}_1` measures how much two variables :math:`x` and :math:`y` vary together, relative to the variability of the independent variable :math:`x` itself. 

Further resources
^^^^^^^^^^^^^^^^^

- `Seeing Theory <https://seeing-theory.brown.edu/regression-analysis/>`__



Assessing the accuracy of the parameter estimates
=================================================

The slope estimator
^^^^^^^^^^^^^^^^^^^

From the OLS solution, we have

.. math:: 

    \hat{\beta}_1 =\frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{\sum{(x_i-\bar{x})^2}}

If we replace :math:`\beta` with :math:`B` (indicating it's a random variable), and replace :math:`y` with :math:`Y`, 
we can write the OLS slope *estimator* :math:`\hat{B}_1` as

.. math:: 
    \hat{B}_1 =\frac{\sum(x_i-\bar{x})(Y_i-\bar{Y})}{\sum(x_i-\bar{x})^2}

Below we show that the slope estimator :math:`\hat{B}_1` follows a normal distribution with the following mean and variance. 

.. math:: 
    \hat{B}_1 \sim \text{N}\bigg(\beta_1, \frac{\sigma^2}{\sum (x_i - \bar{x})^2}\bigg)

To prove it we first show that :math:`\hat{B}_1` is a linear combination of :math:`\hat{Y}_i`'s.

.. admonition:: Theorem

    For :math:`n` sample data :math:`x_1, x_2, \cdots, x_n`, the sum of all deviations from the sample mean :math:`\bar{x}` is zero. 

    **Proof**:

    .. math:: 

         \sum (x_i - \bar{x}) = \sum x_i - \sum \bar{x} = \sum x_i - n \bar{x} = \sum x_i - n \frac{\sum x_i}{n} = \sum x_i - \sum x_i = 0


.. math:: 

    \begin{align}
    \hat{B}_1 &=\frac{\sum(x_i-\bar{x})(Y_i-\bar{Y})}{\sum(x_i-\bar{x})^2} \\
    \\
    &=\frac{\sum\big[(x_i-\bar{x})Y_i - (x_i-\bar{x})\bar{Y}\big]}{\sum(x_i-\bar{x})^2} \\
    \\
    &=\frac{\sum(x_i-\bar{x})Y_i - \sum(x_i-\bar{x})\bar{Y}}{\sum(x_i-\bar{x})^2} \\
    \\
    &=\frac{\sum(x_i-\bar{x})Y_i - \bar{Y}\sum(x_i-\bar{x})}{\sum(x_i-\bar{x})^2} \\
    \\
    &=\frac{\sum(x_i-\bar{x})Y_i - \bar{Y} \cdot 0}{\sum(x_i-\bar{x})^2} \\
    \\
    &=\frac{\sum(x_i-\bar{x})Y_i}{\sum(x_i-\bar{x})^2} \\
    \end{align}

.. admonition:: Theorem

    Any linear combination of independent normally distributed random variables also follows a normal distribution (`see proof <https://statproofbook.github.io/P/norm-lincomb>`__).

Since :math:`Y_i`'s are normally-distributed and independent of each other, :math:`\hat{B}_1`, a linear combination of :math:`Y_i`'s, follows a normal distribution.

Next, we show that the expected value of :math:`\hat{B}_1` is :math:`\beta_1`.

.. math:: 

    \begin{align}
    \text{E}[\hat{B}_1] &= \text{E}\bigg[\frac{\sum (x_i - \bar{x})Y_i}{\sum (x_i - \bar{x})^2}\bigg] \\
    \\
    &=\frac{\sum (x_i - \bar{x})\text{E}[Y_i]}{\sum (x_i - \bar{x})^2} \\
    \\
    &=\frac{\sum (x_i - \bar{x})(\beta_0+\beta_1 x_i)}{\sum (x_i - \bar{x})(x_i - \bar{x})} \\
    \\
    &=\frac{\sum (x_i - \bar{x})\beta_0 +\sum (x_i - \bar{x})\beta_1 x_i}{\sum (x_i - \bar{x})x_i - \sum (x_i - \bar{x})\bar{x}} \\
    \\
    &=\frac{\beta_0\sum (x_i - \bar{x}) + \beta_1 \sum (x_i - \bar{x}) x_i}{\sum (x_i - \bar{x})x_i - \bar{x}\sum (x_i - \bar{x})} \\
    \\
    &=\frac{\beta_0 \cdot 0 + \beta_1 \sum (x_i - \bar{x}) x_i}{\sum (x_i - \bar{x})x_i - \bar{x} \cdot 0} \\
    \\
    &=\frac{\beta_1 \sum (x_i - \bar{x}) x_i}{\sum (x_i - \bar{x})x_i} \\
    \\
    &=\beta_1
    \end{align}

When an estimator's expected value equals the true value of the parameter being estimated, we say that the estimator is `unbiased <https://en.wikipedia.org/wiki/Bias_of_an_estimator>`__.
From the above we show that the OLS slope parameter :math:`\hat{B}_1` is an *unbiased* estimator for the slope parameter :math:`\beta_1` in the simple linear regression model. 

Then, we show that the variance of :math:`\hat{B}_1` is :math:`\frac{\sigma^2}{\sum (x_i - \bar{x})^2}`.

.. math:: 

    \begin{align}
    \text{var}(\hat{B}_1) &= \text{var}\bigg(\frac{\sum (x_i - \bar{x})Y_i}{\sum (x_i - \bar{x})^2}\bigg) \\
    \\
    &= \frac{\sum (x_i - \bar{x})^2\text{var}(Y_i)}{(\sum (x_i - \bar{x})^2)^2} \\
    \\
    &= \frac{\sum (x_i - \bar{x})^2 \sigma^2}{(\sum (x_i - \bar{x})^2)^2} \\
    \\
    &= \frac{\sigma^2 \sum (x_i - \bar{x})^2 }{(\sum (x_i - \bar{x})^2)^2} \\
    \\
    &= \frac{\sigma^2}{\sum (x_i - \bar{x})^2} \\
    \end{align}


.. admonition:: Important

    The OLS slope estimator

    .. math:: 
        \hat{B}_1 \sim \text{N}\bigg(\beta_1, \frac{\sigma^2}{\sum (x_i - \bar{x})^2}\bigg)

In practice, we do not know :math:`\sigma`, the *true* standard deviation of the error term :math:`\epsilon` in the regression model. 
The best thing we can do is to estimate the variance from the data at hand. 

.. math:: 
        \hat{\sigma} = \text{RSE} = \sqrt{\frac{\text{RSS}}{n-2}}=\sqrt{\frac{\sum e_i^2}{n-2}}=\sqrt{\frac{\sum (y_i - \hat{y}_i)^2}{n-2}}

The *estimated* standard deviation :math:`\hat{\sigma}` is often called Residual Standard Error (RSE). 

After we replace :math:`\sigma` with :math:`\hat{\sigma}`, the variance of the slope estimator :math:`\hat{B}_1` becomes

.. math:: 
        \text{var}(\hat{B}_1) = \frac{\sigma^2}{\sum (x_i - \bar{x})^2} \approx \frac{\hat{\sigma}^2}{\sum (x_i - \bar{x})^2} = \frac{\text{RSS}}{(n-2)\sum (x_i - \bar{x})^2} 

Similarly, the standard deviation of the slope estimator :math:`\hat{B}_1`, often called the Standard Error (SE) of the estimator, become

.. math:: 
        \text{SE}(\hat{B}_1) = \sqrt{\frac{\sigma^2}{\sum (x_i - \bar{x})^2}} \approx \sqrt{\frac{\text{RSS}}{(n-2)\sum (x_i - \bar{x})^2}}

After replacing :math:`\sigma` with :math:`\hat{\sigma}`, the standardized version of the slope estimator :math:`\hat{B}_1` follows a `t-distribution <https://en.wikipedia.org/wiki/Student%27s_t-distribution>`__ with degree of freedom of :math:`n-2`.

Confidence interval
^^^^^^^^^^^^^^^^^^^

We can construct a confidence interval (at confidence level :math:`1-\alpha`) for the slope parameter :math:`\beta_1`.

.. math:: 

    \begin{align}
    \text{P}\bigg(-t_{\alpha/2, n-2} < \frac{\hat{B}_1 - \beta_1}{\text{SE}(\hat{B}_1)} < t_{\alpha/2, n-2}\bigg) &= 1-\alpha \\
    \\
    \text{P}\bigg(-t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)  < \hat{B}_1 - \beta_1 < t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)\bigg) &= 1-\alpha \\
    \\
    \text{P}\bigg(-\hat{B}_1 - t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)  < - \beta_1 < - \hat{B}_1 + t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)\bigg) &= 1-\alpha \\
    \\
    \text{P}\bigg(\hat{B}_1 - t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)  < \beta_1 < \hat{B}_1 + t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)\bigg) &= 1-\alpha \\
    \end{align}

Based on the above, we have the confidence interval (at confidence level :math:`1-\alpha`) for the slope parameter :math:`\beta_1` as

.. math:: 

    \bigg[\hat{\beta}_1- t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1),\;\; \hat{\beta}_1+ t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)\bigg]

or simply

.. math:: 

    \hat{\beta}_1 \pm t_{\alpha/2, n-2} \cdot \text{SE}(\hat{B}_1)

where :math:`\hat{\beta}_1` is the OLS estimate of the slope parameter. 


Hypothesis test
^^^^^^^^^^^^^^^

:math:`\text{H}_0`: There is *no* relationship between :math:`x` and :math:`y`.

:math:`\text{H}_a`: There is *some* relationship between :math:`x` and :math:`y`.

Mathematically, this corresponds to test

.. math:: 

    \begin{align}
        \text{H}_0: \beta_1 = 0 \\
        \\
        \text{H}_a: \beta_1 \neq 0 \\
    \end{align}


We compute a t-statistic, given by

.. math:: 

    t=\frac{\hat{\beta}_1 - \beta_1}{\text{SE}(\hat{B}_1)} = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{B}_1)} = \frac{\hat{\beta}_1}{\text{SE}(\hat{B}_1)}


It measures the number of standard deviations that :math:`\hat{\beta}_1` is away from 0. 

If there really is no relationship between :math:`x` and :math:`y`, the t-statistic will have a t-distribution with the degree of freedom of :math:`n-2`.

We reject the null hypothesis :math:`\text{H}_0` if 

.. math:: 

    |t| > t_{\text{critical}}

or 

.. math:: 

    p\text{-value} = 2\cdot \text{P}(t_{n-2} > |t|) < \alpha


Roughly speaking, a small *p*-value means it's unlikely to observe such a relationship due to chance, if there really is *no* relationship. 

Equivalently, we can also check if the confidence interval for :math:`\beta_1` include 0.
If it does, it means the relationship is not significant. 


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

- :math:`\text{H}_0`: There is *no* relationship between :math:`x` and :math:`y`.
- :math:`\text{H}_a`: There is *some* relationship between :math:`x` and :math:`y`.

Mathematically, this corresponds to

.. math:: 

    \begin{align}
        &\text{H}_0: \beta_1 = 0 \\
        \\
        &\text{H}_a: \beta_1 \neq 0 \\
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


Assessing the accuracy of the model 
===================================

Once we reject the null hypothesis :math:`\text{H}_0` 
(i.e., stating that there *is* some relationship between :math:`x` and :math:`y`), 
we want to quantify the *extent* to which the model fits the data. 

A natural thought is to use something that measures the "average amount of errors" that the model made. 
The Residual Standard Error (RSE) that we used previously is such an measure. 

.. math:: 
        \text{RSE} = \sqrt{\frac{\text{RSS}}{n-2}}=\sqrt{\frac{\sum e_i^2}{n-2}}=\sqrt{\frac{\sum (y_i - \hat{y}_i)^2}{n-2}} =\sqrt{\frac{\sum \big(y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i)\big)^2}{n-2}}

RSE provides an *absolute* measure of the model's lack of fit. 
In the advertising example ``sales ~ TV``, the RSE is 3.26 (thousands of units). 
It can be interpreted as the actual sales in each market deviates from the true regression line (the model prediction) by 3,260 units, on average. 

One major limitation of using RSE as a measure of model accuracy is that it is not always clear what constitutes a "good" RSE. 
For example, is an average error of 3,260 units good?

:math:`R^2` statistic
^^^^^^^^^^^^^^^^^^^^^

Compare with the RSE, a more common metric to assess the model accuracy is the :math:`R^2` statistic (sometimes also called the *coefficient of determination*). 

We define the following:

RSS (Residual Sum of Squares)

.. math:: 

    \text{RSS}=\sum_{i=1}^n \big(y_i-\hat{y}_i \big)^2 \text{, where } \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i.

RSS measures the amount of variability in :math:`y` that is *left unexplained* after performing the regression on :math:`x`.

TSS (Total Sum of Squares)

.. math:: 

    \text{TSS}=\sum_{i=1}^n \big(y_i-\bar{y}_i \big)^2 \text{, where } \bar{y}_i = \frac{1}{n}\sum y_i \text{ is the sample mean for } y.

TSS measures the total amount of variability inherent in :math:`y` before performing the regression on :math:`x`.

:math:`\text{TSS}-\text{RSS}` measures the amount of variability in :math:`y` that is explained by performing the regression on :math:`x`.

.. math:: 

    R^2 = \frac{\text{TSS}-\text{RSS}}{\text{TSS}} = 1 - \frac{\text{RSS}}{\text{TSS}}

:math:`R^2` measures the *proportion* of variability in :math:`y` that is explained by performing the regression on :math:`x`.



In the advertising example ``sales ~ TV``, the :math:`R^2` is 0.612. 
It can be interpreted as 61.2% of the variability in the sales can be explained by a regression on the TV budget. 

Notes

- If a model is very accurate, the RSS will be much smaller when compared to TSS, which means the :math:`R^2` will be close to 1. 
- The definition of :math:`R^2` does not rely on any specific form of the model. In fact, it can be computed for *any* model with the output :math:`\hat{y}_i`. 
- For an OLS regression model, it can be proved that :math:`0 \leq R^2 \leq 1`. 
- Generally, :math:`R^2 \geq 0` does *not* hold. Think of an arbitrarily "bad" model.  


Predictions: Confidence and prediction intervals
================================================

Once we fit a regression model to the data, we can use the model to make predictions. 
For example, the model predicts that the sales would be 15,000 units with a TV budget of $100k. 
Often times, in addition to predict a single number of the sales, 
we want to quantify the uncertainty by constructing a interval in which we have high confidence the sales would fall in.


Theorems
^^^^^^^^

Previously, we know the OLS slope estimator :math:`\hat{B}_1` can be written as a linear combination of :math:`Y_i` and follows a normal distribution. 

.. math::

   \hat{B}_1 = \frac{\sum(x_i-\bar{x})Y_i}{\sum(x_i-\bar{x})^2} \sim \text{N}\bigg(\beta_1, \frac{\sigma^2}{S_{xx}}\bigg)

Now we take a look at the OLS intercept estimator :math:`\hat{B}_0`. 

.. math::

   \hat{B}_0 = \bar{Y} - \bar{x}\hat{B}_1

Below we prove that :math:`\hat{B}_0` also follows a normal distribution with the following mean and variance. 

.. math::

    \begin{align}
    \text{E}\big[\hat{B}_0\big] &= \text{E}\big[\bar{Y} - \bar{x}\hat{B}_1\big] \\
    \\
    &= \text{E}\big[\bar{Y}\big] - \bar{x}\text{E}\big[\hat{B}_1\big] \\
    \\
    &= \text{E}\bigg[\frac{1}{n}\sum Y_i\bigg] - \bar{x} \beta_1 \\
    \\
    &= \frac{1}{n}\sum\text{E}\big[ Y_i\big] - \bar{x} \beta_1 \\
    \\
    &= \frac{1}{n}\sum (\beta_0 + \beta_1 x_i) - \bar{x} \beta_1 \\
    \\
    &= \frac{1}{n}(n\beta_0 + \beta_1 \sum x_i) - \bar{x} \beta_1 \\
    \\
    &= \beta_0 + \beta_1 \frac{1}{n}  \sum x_i - \bar{x} \beta_1 \\
    \\
    &= \beta_0 + \beta_1 \bar{x} - \bar{x} \beta_1 \\
    \\
    &= \beta_0 \\
    \end{align}

The above result shows the OLS intercept estimator :math:`\hat{B}_0` is also `unbiased <https://en.wikipedia.org/wiki/Bias_of_an_estimator>`__.


.. math::

    \begin{align}
    \text{var}\big(\hat{B}_0\big) &= \text{var}\big(\bar{Y} - \bar{x}\hat{B}_1\big) \\
    \\
    &= \text{var}\big(\bar{Y}) + \text{var}\big(\bar{x}\hat{B}_1\big) - 2\text{cov}\big(\bar{Y}, \bar{x}\hat{B}_1\big)\\
    \\
    &= \text{var}\bigg(\frac{1}{n}\sum Y_i\bigg) + \bar{x}^2\text{var}\big(\hat{B}_1\big) - 2\bar{x}\text{cov}\big(\bar{Y}, \hat{B}_1\big)\\
    \\
    &= \frac{1}{n^2}\sum \text{var}\big( Y_i\big) + \bar{x}^2 \frac{\sigma^2}{S_{xx}} - 2\bar{x}\cdot 0 \\
    \\
    &= \frac{1}{n^2} n \sigma^2 + \bar{x}^2 \frac{\sigma^2}{S_{xx}} \\
    \\
    &= \sigma^2\bigg(\frac{1}{n}  + \frac{\bar{x}^2}{S_{xx}}\bigg) \\
    \end{align}


In the above proof, we used the fact that :math:`\text{cov}\big(\bar{Y}, \hat{B}_1\big)=0`. 
Below is its proof.

.. math::

    \begin{align}
    \text{cov}\big(\bar{Y}, \hat{B}_1\big) &= \text{cov}\bigg(\frac{1}{n}\sum_i Y_i, \hat{B}_1\bigg) \\
    \\
    &= \frac{1}{n}\text{cov}\big(\sum_i Y_i, \hat{B}_1\big) \\
    \\
    &= \frac{1}{n} \sum_i \text{cov}\big(Y_i, \hat{B}_1\big) \\
    \\
    &= \frac{1}{n} \sum_i \text{cov}\bigg(Y_i, \frac{\sum_j (x_j-\bar{x})Y_j}{S_{xx}}\bigg) \\
    \\
    &= \frac{1}{n S_{xx}} \sum_i \sum_j \text{cov}\big(Y_i, (x_j-\bar{x})Y_j\big) \\
    \\
    &\text{because $\text{cov}(Y_i, Y_i)=0$ when $i \neq j$ ($Y_i$ and $Y_i$ are independent), }\\
    \\
    &= \frac{1}{n S_{xx}} \sum_i (x_i-\bar{x}) \text{cov}(Y_i, Y_i) \\
    \\
    &= \frac{1}{n S_{xx}} \sum_i (x_i-\bar{x}) \text{var}(Y_i) \\
    \\
    &= \frac{1}{n S_{xx}} \sum_i (x_i-\bar{x}) \sigma^2 \\
    \\
    &= \frac{\sigma^2}{n S_{xx}} \sum_i (x_i-\bar{x})  \\
    \\
    &= \frac{\sigma^2}{n S_{xx}} \cdot 0  \\
    \\
    &= 0 \\
    \end{align}


Confidence interval
^^^^^^^^^^^^^^^^^^^

Previously, we compute the model prediction at a given :math:`x=x^*` using the formula below. 

.. math::

    \hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x^*

If we describe the above as a general method of estimating :math:`y` at a given :math:`x=x^*`, we have the estimator for the mean response :math:`\hat{Y}_{\text{mean}, x=x^*}`, or simply :math:`\hat{Y}_{\text{mean}}` as follows.


.. math::

    \hat{Y}_{\text{mean}} = \hat{B}_0 + \hat{B}_1 x^*

Let's construct a confidence interval for :math:`\hat{Y}_{\text{mean}}`, the mean response for all observations at :math:`x=x^*`.

The expected value of :math:`\hat{Y}_{\text{mean}}`:

.. math::

    \begin{align}
    \text{E}\big[\hat{Y}_{\text{mean}} \big] &= \text{E}\big[\hat{B}_0 + \hat{B}_1 x^* \big] \\
    \\
    &= \text{E}\big[\hat{B}_0\big] + \text{E}\big[\hat{B}_1 x^* \big] \\
    \\
    &= \beta_0 + \beta_1 x^* \\
    \end{align}

The variance of :math:`\hat{Y}_{\text{mean}}`:

.. math::

    \begin{align}
    \text{var}\big(\hat{Y}_{\text{mean}} \big) &= \text{var}\big(\hat{B}_0 + \hat{B}_1 x^* \big) \\
    \\
    &=\text{var}\big(\hat{B}_0\big) + \text{var}\big(\hat{B}_1 x^* \big) + 2x^*\text{cov}\big(\hat{B}_0, \hat{B}_1 \big)\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\bigg) + (x^*)^2 \frac{\sigma^2}{S_{xx}} +2 x^* \text{cov}\big(\bar{Y} - \bar{x}\hat{B}_1, \hat{B}_1\big)\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{\bar{x}^2 + (x^*)^2 }{S_{xx}}\bigg) + 2 x^* \bigg[\text{cov}\big(\bar{Y}, \hat{B}_1 \big) - \bar{x}\text{cov}\big(\hat{B}_1, \hat{B}_1\big)\bigg]\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{\bar{x}^2 + (x^*)^2 }{S_{xx}}\bigg) + 2 x^* \big[0 - \bar{x}\text{var}\big(\hat{B}_1\big)\big]\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{\bar{x}^2 + (x^*)^2 }{S_{xx}}\bigg) - 2 x^* \bar{x}\frac{\sigma^2}{S_{xx}}\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{\bar{x}^2 + (x^*)^2 - 2 x^* \bar{x} }{S_{xx}}\bigg)\\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}\bigg)\\
    \end{align}

The standard error of :math:`\hat{Y}_{\text{mean}}`:

.. math::

    \begin{align}
    \text{SE}\big(\hat{Y}_{\text{mean}}\big) &= \sqrt{\text{var}\big(\hat{Y}_{\text{mean}} \big)} \\
    \\
    &= \sqrt{\sigma^2\bigg(\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}\bigg)} \\
    \\
    &= \sigma \sqrt{\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}} \\
    \\
    &\approx \text{RSE} \sqrt{\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}} \\
    \end{align}


After replacing :math:`\sigma` with RSE, the standardized version of :math:`\hat{Y}_{\text{mean}}` follow a *t*-distribution with a degree of freedom of :math:`n-2`.

.. math::

    \frac{\hat{Y}_{\text{mean}} - (\beta_0 + \beta_1 x^*)}{\text{SE}\big(\hat{Y}_{\text{mean}}\big)} \sim t_{n-2}

Using similar approach on constructing the confidence interval, we have the confidence interval (with confidence level :math:`1-\alpha`) for the mean response at :math:`x=x^*`:

.. math::

    \hat{\beta}_0 + \hat{\beta}_1 x^* \pm t_{\alpha/2, n-2} \cdot \text{SE}\big(\hat{Y}_{\text{mean}}\big)

.. note::

    - A confidence interval is used to quantify the uncertainty surrounding the **mean** response over a large number of observations, all at :math:`x=x^*`.
    - The confidence interval for the mean response (:math:`\hat{Y}_{\text{mean}} = \hat{B}_0 + \hat{B}_1 x^*`) captures the uncertainty when we estimate the model parameters (:math:`\beta_0 \text{ and } \beta_1`) based on data.



Prediction interval
^^^^^^^^^^^^^^^^^^^

We use a prediction interval to quantify the uncertainty surrounding the response for a *single* observation at :math:`x=x^*`.

The simple linear regression model takes the form:

.. math:: Y= \beta_0 + \beta_1 \cdot x + \epsilon

For a single observation the estimator of the response:

.. math:: \hat{Y} = \hat{B}_0 + \hat{B}_1 x^* + \epsilon = \hat{Y}_{\text{mean}} + \epsilon

Let's construct a confidence interval for :math:`\hat{Y}`, the response for a single observation at :math:`x=x^*`.

The expected value of :math:`\hat{Y}`:

.. math:: 
    
    \begin{align}
    \text{E}[\hat{Y}] &= \text{E}\big[\hat{Y}_{\text{mean}} + \epsilon \big] \\
    \\
    &= \text{E}\big[\hat{Y}_{\text{mean}}\big] + \text{E}[\epsilon] \\
    \\
    &= \beta_0 + \beta_1 x^* + 0 \\
    \\
    &= \beta_0 + \beta_1 x^* \\
    \end{align}


We see that the expected value of :math:`\hat{Y}` is the same as the expected value of :math:`\hat{Y}_{\text{mean}}`.


The variance of :math:`\hat{Y}`:

.. math::

    \begin{align}
    \text{var}\big(\hat{Y}\big) &= \text{var}\big(\hat{Y}_{\text{mean}} + \epsilon\big)\\
    \\
    &= \text{var}\big(\hat{Y}_{\text{mean}}\big) + \text{var}(\epsilon) + 2 \text{cov}\big(\hat{Y}_{\text{mean}}, \epsilon\big) \\
    \\
    &= \text{var}\big(\hat{Y}_{\text{mean}}\big) + \text{var}(\epsilon) + 2 \text{cov}\big(\hat{B}_0 + \hat{B}_1 x^*, \epsilon\big) \\
    \\
    &\text{As the error $\epsilon$ from a new observation is independent to $\hat{B}_0$ and $\hat{B}_1$}, \\
    \\
    &= \sigma^2\bigg(\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}\bigg) + \sigma^2 + 2 \cdot 0 \\
    \\
    &= \sigma^2\bigg(1 + \frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}\bigg) \\
    \end{align}

The standard error of :math:`\hat{Y}`:

.. math::

    \begin{align}
    \text{SE}\big(\hat{Y}\big) &= \sqrt{\text{var}\big(\hat{Y}\big)} \\
    \\
    &= \sqrt{\sigma^2\bigg(1 + \frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}\bigg)} \\
    \\
    &= \sigma \sqrt{1 + \frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}} \\
    \\
    &\approx \text{RSE} \sqrt{1 + \frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}} \\
    \end{align}


After replacing :math:`\sigma` with RSE, the standardized version of :math:`\hat{Y}` follow a *t*-distribution with a degree of freedom of :math:`n-2`.


.. math::

    \frac{\hat{Y} - (\beta_0 + \beta_1 x^*)}{\text{SE}\big(\hat{Y}\big)} \sim t_{n-2}

Using similar approach, we have the prediction interval (with confidence level :math:`1-\alpha`) for the response to a single observation at :math:`x=x^*`:

.. math::

    \hat{\beta}_0 + \hat{\beta}_1 x^* \pm t_{\alpha/2, n-2} \cdot \text{SE}\big(\hat{Y}\big)


.. note::

    - A prediction interval is used to quantify the uncertainty surrounding the response for a **single** observation at :math:`x=x^*`.
    - From the formula we see the prediction interval is always wider than the confidence interval. 
    - The prediction interval (:math:`\hat{Y} = \hat{B}_0 + \hat{B}_1 x^* + \epsilon`) not only captures the uncertainty when we estimate the model parameters (:math:`\beta_0 \text{ and } \beta_1`), but also the additional uncertainty (:math:`\epsilon`) associated with making prediction for a *single* observation. 


Multiple linear regression
==========================

Introduction
^^^^^^^^^^^^

For the advertising data set, if we want to examine the relationship between all the three media budgets and the sales, 
we can build three simple linear regression models. 

.. math::

    \begin{align}
    \text{sales} &= \beta_0 + \beta_1 \cdot \text{TV} + \epsilon \\
    \\
    \text{sales} &= \beta_0 + \beta_1 \cdot \text{radio} + \epsilon \\
    \\
    \text{sales} &= \beta_0 + \beta_1 \cdot \text{newspaper} + \epsilon \\
    \end{align}

However, a better approach would be to build one linear regression model that incorporating all the three media. 
We can give each independent variable a separate slope parameter. 

.. math:: 
    
    \text{sales} = \beta_0 + \beta_1 \cdot \text{TV} + \beta_2 \cdot \text{radio} + \beta_3 \cdot \text{newspaper}+ \epsilon

This is called a *multiple* linear regression model, as there are multiple independent variables in the model. 

In general, a multiple linear regression model takes the form:

.. math:: 
    
    Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \epsilon

where

- :math:`x_1, x_2, \cdots, x_p` are :math:`p` independent variables;
- :math:`\beta_i` is the slope parameter associated with independent variable :math:`x_i` where :math:`i=1, 2, \cdots, p`;
- :math:`\beta_0` is the intercept parameter;
- :math:`\epsilon` is the same error term in the simple linear regression that followings a normal distribution with a mean of 0 and variance of :math:`\sigma^2`.
- :math:`Y` is the dependent variable.

As was the case in the simple linear regression, the model parameters (:math:`\beta_0, \beta_1, \beta_2, \cdots, \beta_p`) are unknown and need to be estimated based on data. 

We can see :math:`Y` is a normally-distributed random variable, as it is a normally-distributed random variable :math:`\epsilon` plus some non-random value. 

The expected value of :math:`Y`:

.. math::

    \begin{align}
    \text{E}[Y] &= \text{E}[\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \epsilon] \\
    \\
    &= \text{E}[\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p] + \text{E}[\epsilon] \\
    \\
    &= \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + 0 \\
    \\
    &= \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p \\
    \end{align}

Interpretations of the model parameters

- The intercept parameter :math:`\beta_0` can be interpreted as the expected value of :math:`Y` when :math:`x_1=x_2=\cdots=x_p=0`.
- The slope parameter :math:`\beta_i` can be interpreted as the expected change of :math:`Y` per unit change of :math:`x_i`, *holding all other independent variables fixed*. 

The variance of :math:`Y`:

.. math::

    \begin{align}
    \text{var}(Y) &= \text{var}(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \epsilon) \\
    \\
    &= \text{var}(\epsilon) \\
    \\
    &= \sigma^2
    \end{align}

In summary, we have

.. math:: Y \sim \text{N}(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p, \;\sigma^2)


Parameter estimation
^^^^^^^^^^^^^^^^^^^^

Previously for simple linear regression, we used a method called Ordinary Least Squares (OLS) that finds the parameters that minimizes the RSS (residual sum of squares). 
For multiple linear regression we used the same approach. 
We choose :math:`\hat{\beta}_0, \hat{\beta}_1, \cdots, \hat{\beta}_p` such that the RSS is minimized. 


.. math:: \min_{\beta_0, \beta_1, \cdots, \beta_p} \bigg\{ f(\beta_0, \beta_1, \cdots, \beta_p)=\text{RSS}= \sum \big[y_i - (\beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p )\big]^2 \bigg\}

The above minimization problem can be solved using the method Maximum Likelihood Estimate (MLE). 
The form of the solution is somewhat complex. 
In this course we rely on software packages such as the ``statsmodels`` library in Python to compute the solution for us. 


Model utility test
^^^^^^^^^^^^^^^^^^

With a fitted multiple linear regression model, the first question we may ask is "*Is the model useful at all?*"
We can answer this question by a hypothesis test called *model utility test* or F-test.

- :math:`\text{H}_0`: The model is *not* useful at all.
- :math:`\text{H}_a`: The model is at least somewhat useful.

Mathematically, this corresponds to

.. math:: 

    \begin{align}
        &\text{H}_0: \beta_1 = \beta_2 = \cdots = \beta_p = 0 \\
        \\
        &\text{H}_a: \text{at least one } \beta_j \text{ is not zero.} \\
    \end{align}


We compute the F-statistic

.. math:: F = \frac{(\text{TSS}-\text{RSS})/p}{\text{RSS}/(n-p-1)}

- The numerator :math:`(\text{TSS}-\text{RSS})/p` measures the variability that can be explained by the model. 
- The denominator :math:`\text{RSS}/(n-p-1)` measures the variability that can *not* be explained by the model. 

Roughly speaking, if a model is useful, the RSS is small, and the F-statistic is large. 

If the null hypothesis :math:`H_0` is true, the F-statistic follows a `F-distribution <https://en.wikipedia.org/wiki/F-distribution>`__ with degrees of freedom of :math:`p` and :math:`n-p-1`. 
We reject the null hypothesis if the F-statistic is greater than the critical value :math:`F_{\alpha, p, n-p-1}`.
Equivalently, we reject the null hypothesis if the *p*-value is less than the significant level :math:`\alpha`.


.. list-table:: ANOVA (Analysis of variance) table
   :widths: 15 15 30 30 30
   :header-rows: 1

   * - 
     - df
     - Sum of squares
     - Mean squares
     - F
   * - Regression
     - :math:`p`
     - :math:`\text{TSS} - \text{RSS}`
     - :math:`(\text{TSS} - \text{RSS})/p`
     - :math:`F=\frac{(\text{TSS}-\text{RSS})/p}{\text{RSS}/(n-p-1)}`
   * - Residual
     - :math:`n-p-1`
     - :math:`\text{RSS}=\sum (y_i-\hat{y}_i)^2`
     - :math:`\text{RSS}/(n-p-1)`
     - 
   * - Total
     - :math:`n-1`
     - :math:`\text{TSS}=\sum (y_i-\bar{y})^2`
     - 
     -






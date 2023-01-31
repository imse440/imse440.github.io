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


Visualize :math:`\beta_0` and :math:`\beta_1`


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

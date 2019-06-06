def ll_heatmap(alpha_max, beta_max, n_data, res, fig_name):
    alpha0 = np.linspace(0, alpha_max, n_data)
    beta0 = np.linspace(0, beta_max, n_data)

    ll = np.zeros((n_data, n_data))
    for i, B0 in enumerate(alpha0):
        for j, B1 in enumerate(beta0):
            ll[i, j] = -neg_likelihood([B0, B1], reward, action)

    fig, ax = plt.subplots()

    # We need to draw the canvas, otherwise the labels won't be positioned and
    # won't have values yet.
    fig.canvas.draw()

    # labels_x = [item.get_text() for item in ax.get_xticklabels()]
    labels_y = np.linspace(alpha_max, 0, 6)

    ax.set_yticklabels(labels_y)
    labels_x = np.linspace(0, beta_max, 6)

    ax.set_xticklabels(labels_x)

    x = (alpha_max - res.x[0]) / (alpha_max / (n_data - 1))
    y = res.x[1] / (beta_max / (n_data - 1))

    fig = plt.imshow(ll, cmap='hot', interpolation='none')
    fig = plt.plot(y, x, 'bo')

    fig = plt.xlim((0, n_data))
    fig = plt.ylim((0, n_data))

    plt.xlabel('beta')
    plt.ylabel('alpha')
    plt.title('log likelihood')

    plt.colorbar()

    plt.savefig(fig_name)
    plt.show()

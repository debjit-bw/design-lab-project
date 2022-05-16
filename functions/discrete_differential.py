def d_dt(y_vals, timestamps):
    d_dt = []
    for i in range(1, len(y_vals)):
        if timestamps[i] - timestamps[i - 1] != 0:
            val = (y_vals[i] - y_vals[i-1]) / (timestamps[i] - timestamps[i-1])
            if val != 0:
                d_dt.append(val)
            else:
                d_dt.append(d_dt[-1])
    return d_dt
# Seung-Chan Kim

def get_sparse_idx(data_in, nStride):
    data_out =[]
    for i in range(data_in.shape[0]):
        if i % nStride == 0:
            data_out.append(data_in[i,:])

    return data_out


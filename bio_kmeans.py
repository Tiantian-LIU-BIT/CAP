# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 09:27:29 2020

@author: tiantian
"""

import numpy as np
import scipy.io as scio
from Bio.Cluster import kcluster
import os
from sklearn.metrics import silhouette_score


#all_data=np.zeros(shape=(122237,1024))#487被试一起
#all_data=np.zeros(shape=(130269,1024))#519被试一起
all_data=np.zeros(shape=(137297,1024))#547被试一起
#all_data=np.zeros(shape=(15311,1024))#仅有20岁的
#all_data=np.zeros(shape=(23594,1024))#仅有70岁的
sub_id=0
for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y20_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y20_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))
    
for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y30_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y30_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))

for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y40_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y40_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))
    
for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y50_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y50_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))
    
for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y60_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y60_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))

for info in os.listdir(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y70_mat'):
    domain=os.path.abspath(r'F:\research\Aging_cluster\FunImgARFWSglobalC\y70_mat')
    sub_id=sub_id+1
    info=os.path.join(domain,info)
    dataMatlab=scio.loadmat(info)
    all_data[(sub_id-1)*251:(sub_id*251)]=np.transpose(np.transpose(dataMatlab['ROISignals']))

K=range(16,21)
clusterid_all=[]
error_all=[]
nfound_all=[]

for k in K:
    clusterid,error,nfound=kcluster(all_data,k,dist='c',npass=15)
    #silhouette_avg = silhouette_score(all_data, clusterid, metric = 'correlation')
    #error是最优解中，每类内距离的总和
    kk = '%02d' % k

    save_fn1 = str.format('F://research//Aging_cluster//clusterid'+str(kk)+'.mat')
    scio.savemat(save_fn1, {'clusterid': clusterid})
    
    save_fn2 = str.format('F://research//Aging_cluster//error'+str(kk)+'.mat')
    scio.savemat(save_fn2, {'error': error})
    
    save_fn3 = str.format('F://research//Aging_cluster//nfound'+str(kk)+'.mat')
    scio.savemat(save_fn3, {'nfound': nfound})
    
    #save_fn4 = str.format('F://research//Aging_cluster//silhouette_avg'+str(kk)+'.mat')
    #scio.savemat(save_fn4, {'silhouette_avg': silhouette_avg})


"""
__author__ = chrislaw
__project__ = SecureStateEstimation
__date__ = 10/5/18
"""
""" draw the figure used in paper
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rc('text', usetex=True)
plt.rcParams.update({'font.size': 13, 'legend.fontsize':10})

# --------------------------------------- level vs iteration --------------------------------------
# with open('over2', 'rb') as filehandle:
#     level = pickle.load(filehandle)
# fig, ax = plt.subplots(2, 2)
# ax[0][0].text(27, -9.5, '(a)' )
# ax[0][0].plot(range(1, len(level) + 1), level)
# ax[0][0].set_xlabel(r'Iteration', usetex=True )
# ax[0][0].set_ylabel(r'level', usetex=True)
# ax[0][0].set_xticks([0, 20, 40, 60])
# ax[0][0].set_yticks([0, 5, 10, 15, 20])

# with open('over3', 'rb') as filehandle:
#     level = pickle.load(filehandle)
# ax[0][1].plot(range(1, len(level) + 1), level)
# ax[0][1].set_xlabel(r'Iteration', usetex=True )
# ax[0][1].set_ylabel(r'level', usetex=True)
# ax[0][1].set_yticks([0, 5, 10, 15, 20])
# ax[0][1].text(200, -9.5, '(b)' )
#
# with open('over3_r3', 'rb') as filehandle:
#     level = pickle.load(filehandle)
# ax[1][0].plot(range(1, len(level) + 1), level)
# ax[1][0].set_xlabel(r'Iteration', usetex=True )
# ax[1][0].set_ylabel(r'level', usetex=True)
# ax[1][0].set_yticks([0, 5, 10, 15, 20])
# ax[1][0].text(17, -9.5, '(c)' )
#
# with open('over3_r4', 'rb') as filehandle:
#     level = pickle.load(filehandle)
# ax[1][1].plot(range(1, len(level) + 1), level)
# ax[1][1].set_xlabel(r'Iteration', usetex=True )
# ax[1][1].set_ylabel(r'level', usetex=True)
# ax[1][1].set_yticks([0, 5, 10, 15, 20])
# ax[1][1].text(36, -9.5, '(d)' )
#
#
# fig.tight_layout()
# plt.show()

# --------------------------------------- n varies with noiseless --------------------------------------
# smt = np.array([0.154398249700000,	0.155091903300000,	0.0978938188000000,	0.190196719900000,	0.261311356100000,	0.5363312293000005])
# search = np.array([0.009015, 0.013133, 0.032277, 0.041411, 0.171899, 0.361232])
# miqp = np.array([0.05584859999999999, 0.07601880000000001, 0.0270188, 0.29438919999999996, 0.3030236, 0.2623014 ])
#
# n = np.array([10, 25, 50, 75, 100, 150])

# smt_error = np.array([3.38569233839563e-16,	1.95818672448298e-15,	3.89344813365748e-14,	4.09295088643850e-12,	3.05051986671621e-09,
#                       0.000481281063203100])
# search_error = np.array([1.2730451658146966e-15, 3.0229509803775837e-15, 7.660902400161737e-14, 3.885420093390361e-12,
#                          3.450610400660245e-09, 4.5971654934011094e-05])
#
# miqp_error = np.array([1.2730451658146966e-15,  2.3916064556910426e-15, 7.660902400161737e-14, 3.88542009339036e-12,
#                        3.19662730528689e-11, 4.597165493401109e-05])
#
#
# fig, ax = plt.subplots(2, 1)
#
# l2 = ax[0].plot(n, smt, 'r--o')
# l3 = ax[0].plot(n, miqp, 'g--s')
# l1 = ax[0].plot(n, search, 'b--d')
#
# ax[0].legend([r'IMHOTEP-SMT', r'MIQCP', r'Alg.1'])
# ax[0].set_xlabel(r'Number of states $n$', usetex=True )
# ax[0].set_ylabel(r'Execution time (sec)', usetex=True)
#
# ax[1].semilogy(n, smt_error, 'r--o')
# ax[1].semilogy(n, miqp_error, 'g--s')
# ax[1].semilogy(n, search_error, 'b--d')
#
# # plt.legend([r'Alg.1', r'IMHOTEP-SMT'])
# ax[1].set_xlabel(r'Number of states $n$', usetex=True)
# ax[1].set_ylabel(r'$\|x^* - x_0\|_2 / \|x_0\|_2$', usetex=True)
#
# fig.tight_layout()
# plt.savefig('/Users/chrislaw/Box Sync/SSE/figure/vs_n.pdf', bbox_inches='tight', dpi=600)
# plt.show()

# -------------------------------- n varies with noise --------------------------------------
# smt = np.array([0.0781434985,	0.122485432 ,	0.8048681509,	2.0928267022,	2.7799694334 ])
# search = np.array([0.032514, 0.06062970000000001, 0.24615689999999998, 0.5385632, 0.9219160000000001])
# miqp = np.array([0.21515560000000003 , 0.23209439999999998, 0.1325947 , 0.1031791 , 2.3552104])
#
# n = np.array([10, 25, 50, 75, 100])
#
# smt_error = np.array([0.0651489632924267,	0.0670064026429532,	0.247245924625395,	 0.837347679516703,	11.3699118057494,
#                      ])
# search_error = np.array([0.0651489632924266, 0.06700640264295318, 0.2472459246253953, 0.837347679516696,
#                          11.369911805750544])
#
# miqp_error = np.array([0.0651489632924266,  0.06700640264295317, 0.4620594821152243, 0.8373476795166959, 11.369911805750542])
#
#
# fig, ax = plt.subplots(2, 1)
#
# l2 = ax[0].plot(n, smt, 'r--o')
# l3 = ax[0].plot(n, miqp, 'g--s')
# l1 = ax[0].plot(n, search, 'b--d')
#
# ax[0].legend([r'IMHOTEP-SMT', r'MIQCP', r'Alg.1'])
# ax[0].set_xlabel(r'Number of states $n$', usetex=True )
# ax[0].set_ylabel(r'Execution time (sec)', usetex=True)
#
# ax[1].semilogy(n, smt_error, 'r--o')
# ax[1].semilogy(n, miqp_error, 'g--s')
# ax[1].semilogy(n, search_error, 'b--d')
#
# # plt.legend([r'Alg.1', r'IMHOTEP-SMT'])
# ax[1].set_xlabel(r'Number of states $n$', usetex=True)
# ax[1].set_ylabel(r'$\|x^* - x_0\|_2 / \|x_0\|_2$', usetex=True)
#
# fig.tight_layout()
#
# plt.savefig('/Users/chrislaw/Box Sync/SSE/figure/noise_vs_n.pdf', bbox_inches='tight', dpi=600)
# plt.show()

# ----------------------------------- p varies with noiseless -------------------------
# smt = np.array([0.00517343650000000,	0.0900785035000000,	0.292310873900000,	0.587996512200000,	1.08013216610000,	2.04450678640000])
# search = np.array([0.001249, 0.017305, 0.059303, 0.09473, 0.155242, 0.271379])
# miqp = np.array([0.009306100000000001, 0.08076740000000002, 0.13222209999999998, 0.9207647999999999, 0.5926137, 3.1207153999999995 ])
#
# p = np.array([3, 30, 60, 90, 120, 150])
#
# smt_error = np.array([3.94300156107503e-13,	9.43331534203525e-16,	8.25980683692100e-16,	6.21825516131406e-16,	7.54161309646470e-16,
# 	8.14853383136167e-16])
# search_error = np.array([1.9985174439237436e-13, 3.714474161369242e-15, 1.6162963019025597e-15,
#                           3.654963358195414e-15, 2.494607697774148e-15, 3.151280538128965e-15])
#
# miqp_error = np.array([1.9985174439237436e-13, 3.714474161369242e-15, 1.6162963019025597e-15, 3.654963358195415e-15,
#                  1.3859244380905137e-15,  3.151280538128965e-15])
#
# fig, ax = plt.subplots(2, 1)
# # plt.rc('text', usetex=True)
# # plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
# l2 = ax[0].plot(p, smt, 'r--o')
# l3 = ax[0].plot(p, miqp, 'g--s')
# l1 = ax[0].plot(p, search, 'b--d')
# ax[0].legend([r'IMHOTEP-SMT', r'MIQCP', r'Alg.1' ])
# ax[0].set_xlabel(r'Number of sensors $p$', usetex=True)
# ax[0].set_ylabel(r'Execution time (sec)', usetex=True)
# # ax[0].set_xticks([0, 30, 60, 90, 120, 150])
#
# # ax[0].set_ylim(-0.02, 0.8)
# # ax[0].set_yticks([0,  0.2, 0.4, 0.6,  0.8])
#
# ax[1].semilogy(p, smt_error, 'r--o')
# ax[1].semilogy(p, miqp_error, 'g--s')
# ax[1].semilogy(p, search_error, 'b--d')
# ax[1].set_xlabel(r'Number of sensors $p$', usetex=True)
# ax[1].set_ylabel(r'$\|x^* - x_0\|_2 / \|x_0\|_2$', usetex=True)
#
# fig.tight_layout()
#
# plt.savefig('/Users/chrislaw/Box Sync/SSE/figure/vs_p.pdf', bbox_inches='tight', dpi=600)
# plt.show()


# ----------------------------------- p varies with noise -------------------------
smt = np.array([0.0368, 0.1512, 0.3652, 0.7180, 1.8322])
search = np.array([0.0246005,0.0723677 ,0.10271029999999999 ,0.15601530000000002 ,0.2338597])
miqp = np.array([0.012554899999999999 ,0.10243390000000001 ,1.1023882999999999, 0.8653587 ,0.8414181])

p = np.array([30, 60, 90, 120, 150])

smt_error = np.array([0.1963, 0.0964, 0.1218,  0.0450, 0.1073])
search_error = np.array([0.19629878493085373,0.09637933564464105,0.12177113314118601, 0.04504335773165751,0.10726913107924596])

miqp_error = np.array([ 0.2096793221625214, 0.096379335644641, 0.12177113314118605, 0.04504335773165751,  0.10726913107924596])

fig, ax = plt.subplots(2, 1)
l2 = ax[0].plot(p, smt, 'r--o')
l3 = ax[0].plot(p, miqp, 'g--s')
l1 = ax[0].plot(p, search, 'b--d')

ax[0].legend([r'IMHOTEP-SMT', r'MIQCP', r'Alg.1'])
ax[0].set_xlabel(r'Number of sensors $p$', usetex=True)
ax[0].set_ylabel(r'Execution time (sec)', usetex=True)

ax[0].set_yticks([0,  0.5, 1.0, 1.5,  2.0])

ax[1].semilogy(p, smt_error, 'r--o')
ax[1].semilogy(p, miqp_error, 'g--s')
ax[1].semilogy(p, search_error, 'b--d')

ax[1].set_xlabel(r'Number of sensors $p$', usetex=True)
ax[1].set_ylabel(r'$\|x^* - x_0\|_2 / \|x_0\|_2$', usetex=True)

# fig.legend((l1, l2), ('Alg.1', 'IMHOTEP-SMT'), 'lower center')
fig.tight_layout()

plt.savefig('/Users/chrislaw/Box Sync/SSE/figure/noise_vs_p.pdf', bbox_inches='tight', dpi=600)
plt.show()

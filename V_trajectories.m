function V_trajectories
% ------------------------------------------------------------------------------
% 2021-07-31
% 2021-08-26 finally done in Mathematica, however...
%
% Several trajectories connecting different matrices on the ep-gt plane.
% This includes W = the best orthogonal approximation of AME(4, 6) (so far).
% More details in https://arxiv.org/abs/2204.12470
% ------------------------------------------------------------------------------

    addpath ../matrix_tool
    hold all;
    draw_edges(0.985);
    P = P36(3);
    Q = Q36;
    V = V36; # == W5 (some generic pattern, see: https://arxiv.org/abs/2204.12470)

    scatter(e_p(P), g_t(P), 25, "k", "filled");
    scatter(e_p(P*swap(6)), g_t(P*swap(6)), 25, "g", "filled");

    scatter(e_p(Q), g_t(Q), 25, "b", "filled");
    scatter(e_p(V), g_t(V), 25, "m", "filled");
    scatter(1, 1, 25, "k", "filled");

    % trajetory from P_36 to Q^*
    for t=0:0.05:1%pi/2
        p = pi*[t*5/6, 0, 0, 0, 0, t*1/6];
        U = eye(36);
        U( 3: 4, 3: 4) = RTheta(p(1));
        U( 9:10, 9:10) = RTheta(p(2));
        U(15:16,15:16) = RTheta(p(3));
        U(21:22,21:22) = RTheta(p(4));
        U(27:28,27:28) = RTheta(p(5));
        U(33:34,33:34) = RTheta(p(6));
        U = U*P;
        scatter(e_p(U), g_t(U), 1, "b", "filled");
    end

    % trajectory from Q^* to V^*
    for t=0:0.01:1
        p = pi*[  t,  t,  0,  0, -t, -t]; % bottom edge
        p = pi*[  t, -t, -t, -t, -t, -t]; % horizontal line
        p = pi*[  t,  t,  t, -t, -t, -t]; % vertical line
        p = pi*[ -t,  t,  t,  t,  t, -t]; % vertical line

        U = eye(36);
        U( 3: 4, 3: 4) = RTheta(p(1));
        U( 9:10, 9:10) = RTheta(p(2));
        U(15:16,15:16) = RTheta(p(3));
        U(21:22,21:22) = RTheta(p(4));
        U(27:28,27:28) = RTheta(p(5));
        U(33:34,33:34) = RTheta(p(6));

%        U = zeros(36);
%        for j=1:18
%            U(2*j-1:2*j,2*j-1:2*j) = RTheta(p(j));
%        end
        U = U*P;
        scatter(e_p(U), g_t(U), 1, "k", "filled");
    end

end

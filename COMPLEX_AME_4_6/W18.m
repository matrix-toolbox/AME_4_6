function W18
% ------------------------------------------------------------------------------
% 2018-11-02
% 2021-07-26
% 2021-07-30
% 2021-08-26
%
% Best orthogonal approximation of AME(4, 6).
% The "most" general form with 18 2x2 unitary blocks overlapping ones
% in the permutation matrix P = P36(3) (by Clarisse...).
% Details in https://arxiv.org/abs/2204.12470
% ------------------------------------------------------------------------------

    T = P36(3);              % initial permutation matrix
    e_max = -Inf;
    p = rand(1,18)*2.0*pi;   % phases
    U = direct_sum(T, p);     % permutation matrix with additional phases
    mu = 0.1;
    for j = 0:1e+15;
        RESTORE_p=p;
        p = mod(p + randn(1,18) * mu, 2.0*pi);
        %p(1)=1*pi/5; % fixing some elements makes it easier to recover analytical form of the others
        p(2)=5*pi/6; % usually they are k*pi/12 (for integer k) but it is not a general rule!
        p(17)=1*pi/6;
        p_DEBUG = pi./p; % <-- to recover nice analytical values
        U = direct_sum(T, p);
        e = e_p(U);
        if e > e_max
            e_max = e;
            printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t\tep=%4.15g\n", p(1),p(2),p(3),p(4),p(5),p(6),p(7),p(8),p(9),p(10),p(11),p(12),p(13),p(14),p(15),p(16),p(17),p(18), e_max);
            save("xxxxxxxxxxxxxx0826.dat", "*");
        else
           p=RESTORE_p;
        end
        mu = (1.0 - e_max) * 0.05;
    end
end

% Extended template with 18 rotation matrices of size 2x2.
% We start with a direct sum (block diagonal matrix) and transform it back to P36.
function U = direct_sum(T, p)
    U = zeros(36);
    for j=1:18
        U(2*j-1:2*j,2*j-1:2*j) = RTheta(p(j));
    end
    U = U * T;
end





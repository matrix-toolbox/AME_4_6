function U = W6()
% ------------------------------------------------------------------------------
% 2018-11-01
% 2021-07-31
%
% Best orthogonal approximation of AME(4, 6).
% RANDOM WALK over 6 2x2 blocks introduced into P36(3) (by Clarisse...).
% See W5.m -- reduced form.
% ------------------------------------------------------------------------------

    more off
    fflush(stdout)
    clc

    T = P36(3); % Clarisse et al. ...

    e_max = -Inf;
    p = rand(1,6)*2.0*pi;   % phases
    U = direct_sum(T, p);   % permutation matrix with additional phases
    mu = 0.1;
    for j = 0:1e+15;
        RESTORE_p = p;
        p = mod(p + randn(1,6) * mu, 2.0*pi);
        p(1) = pi*5/6;
        p(4) = 0;
        %p(6) = pi*1/6;
        %p(2) = 0; % fixed component of p
        %p(5) = 0; % zero at p2 and p4 recovers matrix G of Grzesiek, other pj values are in W36p6_1040.dat
        p_DEBUG = p/pi;
        U = direct_sum(T, p);
        e = e_p(U);
        if e > e_max
            e_max = e;
            printf("%d\t%d\t%d\t%d\t%d\t%d \t ep=%4.15g\n", p(1),p(2),p(3),p(4),p(5),p(6), e_max);
            save("_xxxxxxxFNAME", '*');
        else
           p = RESTORE_p;
        end
        mu = (1 - e_max) * 0.5;
    end
end


function U = direct_sum(T, p)
    U = eye(36);
    U( 3: 4, 3: 4) = RTheta(p(1));
    U( 9:10, 9:10) = RTheta(p(2));
    U(15:16,15:16) = RTheta(p(3));
    U(21:22,21:22) = RTheta(p(4));
    U(27:28,27:28) = RTheta(p(5));
    U(33:34,33:34) = RTheta(p(6));
    U = U*T;
end



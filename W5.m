function U = W5()
% ------------------------------------------------------------------------------
% 2021-09-05
%
% Best orthogonal approximation of AME(4, 6) so far...
% ------------------------------------------------------------------------------

    T = P36(3); % Clarisse et al.

    p = pi*[5/6, 23/12, 1/12, 0, 7/6, 5/4];
    U = direct_sum(p)*T;

end

function U = direct_sum(p)
    U = eye(36);
    U( 3: 4, 3: 4) = RTheta(p(1));
    U( 9:10, 9:10) = RTheta(p(2));
    U(15:16,15:16) = RTheta(p(3));
    U(21:22,21:22) = RTheta(p(4));
    U(27:28,27:28) = RTheta(p(5));
    U(33:34,33:34) = RTheta(p(6));
end
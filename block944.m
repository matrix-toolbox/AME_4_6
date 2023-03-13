function block944
% ------------------------------------------------------------------------------
% 2022-03-26
%
% AME46 as U^G transformed into a 9x(4x4) block form with two permutations.
% Compare with "AME_beautifier.[m|nb]"...
%
% See also: https://github.com/matrix-toolbox/AME_4_6
% for additional (required) M-scripts.
% ------------------------------------------------------------------------------

    addpath ../AME46
    addpath ../matrix_tool

    a = sqrt(1 - 1 / sqrt(5)) / 2;
    b = sqrt(1 + 1 / sqrt(5)) / 2;
    c = 1/sqrt(2);
    assert(abs(a*a + b*b - c*c) < 1e-12, true)

    U = AME46_ORIGINAL();
    U = Tx(U, 2, [6 6]);

    U3c = zeros(36);
    for j=1:36
    for k=1:36
        if abs(abs(U(j, k)) - a) < 1e-10
            U3c(j, k) = 1;
        end

        if abs(abs(U(j, k)) - b) < 1e-10
            U3c(j, k) = 2;
        end

        if abs(abs(U(j, k)) - c) < 1e-10
            U3c(j, k) = 3;
        end
    end, end

    P1 = [
        0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0;
        0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 6
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0; % 12
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 18
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1;
        0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 24
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 30
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 36
    ];


    P2 = [
        0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0;
        0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0; % 6
        0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0;
        0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0; % 12
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 18
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 1 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0; % 24
        0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 1 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,1 0 0 0 0 0,0 0 0 0 0 0; % 30
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 1 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 1,0 0 0 0 0 0,0 0 0 0 0 0;
        0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 1 0 0 0 0,0 0 0 0 0 0; % 36
    ];

    assert(norm(P1 * transpose(P1) - eye(36), "fro") < 1e-15, true)
    assert(norm(P2 * transpose(P2) - eye(36), "fro") < 1e-15, true)

    b944 = P1 * U3c * P2;

    % each 4x4 matrix u is unitary
    % additionally, for each u, each sub-block 2x2 is unitary too!
    for j=1:9
        u=(P1 * U * P2)((j - 1) * 4 + 1:(j - 1) * 4 + 4, (j - 1) * 4 + 1:(j - 1) * 4 + 4);
        assert(norm(u*u'-eye(4), "fro") < 1e-14)
        u1=u(1:2, 1:2)*sqrt(2);
        assert(norm(u1*u1'-eye(2), "fro") < 1e-13)
        u2=u(1:2, 3:4)*sqrt(2);
        assert(norm(u2*u2'-eye(2), "fro") < 1e-13)
        u3=u(3:4, 1:2)*sqrt(2);
        assert(norm(u3*u3'-eye(2), "fro") < 1e-13)
        u4=u(3:4, 3:4)*sqrt(2);
        assert(norm(u4*u4'-eye(2), "fro") < 1e-13)
    end

    a
    b
    c
    abs((P1 * U * P2)(30:36, 30:36))

    color_map = [1 1 1; 1 0 0; 0 1 0; 0 0 1]; % custom color map
    clf
    colormap(color_map);
    subplot(1,2,1), imagesc(U3c)
    axis([0,37,0,37], "square");
    set(gca, 'xtick', 0:6:36);
    set(gca, 'ytick', 0:6:36);
    subplot(1,2,2), imagesc(b944)
    axis([0,37,0,37], "square");
    set(gca, 'xtick', 0:6:36);
    set(gca, 'ytick', 0:6:36);
    printcf(b944)

end

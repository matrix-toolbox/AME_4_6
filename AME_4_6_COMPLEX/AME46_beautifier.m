function BDForm = AME46_beautifier
% ------------------------------------------------------------------------------
% 2021-01-12 AME beautifier... FIRST VERSION
% 2021-09-01
% 2023-03-08
%
% Two diagonal matrices bring AME46 to a symmetric block diagonal form
% with 9 blocks, each of size 4x4.
% The resulting form is visually symmetric along the center.
%
% See also: "block944.m".
% ------------------------------------------------------------------------------

    o = 0;

    PR = [
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o;
    ];

    PC = [
	o, o, o, o, o, o, o, o, o, 1, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, 0, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0;
	0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, 1, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, 0, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, 1, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, 1, o, o, o, o, o;
	o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o;
	o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o;
	o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, 1, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, 0, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, 0, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, 0, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, 0, o, o, o, o, o, o;
	o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, 1, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, 0, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, 0, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o;
	o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, 1, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o
    ];

    BDForm = PR*AME46*PC;
    printcf(BDForm);
    hold all
    axis("square");
    imshow(abs(BDForm));

end

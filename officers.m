function officers(type)
% -----------------------------------------------------------------------------
% 2022-03-06
%
% Full system of Eqs.(5) from [https://arxiv.org/pdf/2104.05122.pdf].
% Each row of U represents one (quantum) officer.
%
% -----------------------------------------------------------------------------
%
% Call:
% >> officers('quhex') % for physical notation
% or
% >> officers('chess') % for qChess notation
% or
% >> officers('cHTML') % for HTML notation
%
% -----------------------------------------------------------------------------
% 2022-03-25 improved display
% -----------------------------------------------------------------------------

    addpath ../AME46
    addpath ../matrix_tool
    U = T(AME46_ORIGINAL);

    FROM_ZERO = true;  % if true then kets are numbered from 0 to 5, otherwise 1 to 6

    a = sqrt(1 - 1 / sqrt(5)) / 2;
    b = sqrt(1 + 1 / sqrt(5)) / 2;
    c = 1 / sqrt(2);
    assert(abs(a*a + b*b - c*c)<1e-12, true)

    for j=1:36
	ROW = U(j, :);
	ket_psi = '';
	non_empty = 0;
	for k=1:36
	    if ROW(k) != 0
		if non_empty
		    ket_psi = strcat(ket_psi, ' + ');
		end

		w=U(j,k);
		if abs(abs(w)-a)<1e-10
			ket_psi = strcat(ket_psi, 'a');
		end
		if abs(abs(w)-b)<1e-10
			ket_psi = strcat(ket_psi, 'b');
		end
		if abs(abs(w)-c)<1e-10
			ket_psi = strcat(ket_psi, 'c');
		end
		
		phase = fix(round(mod(20+arg(w)/pi*10,20)));
		if phase == 1
		    if type=='cHTML'
		        ket_psi = strcat(ket_psi, '&omega;');
		    else
                        ket_psi = strcat(ket_psi, '\omega');
                    end
                elseif phase != 0
                    if type=='cHTML'
                        ket_psi = strcat(ket_psi, '&omega;<sup>', num2str(phase), '</sup>');
                    else
                        ket_psi = strcat(ket_psi, '\omega^{', num2str(phase), '}');
                    end
                endif

                ket_psi = strcat(ket_psi, '|');
		if type=='chess'
		    ket_psi = strcat(ket_psi, '{\color{', c2color(k), '}', c2chess(k), '}');
		end
		if type=='quhex' || type=='cHTML'
		    ket_psi = strcat(ket_psi, num2str(floor((k-1)/6)+1)-FROM_ZERO);
		    ket_psi = strcat(ket_psi, num2str(mod(k-1,6)+1)-FROM_ZERO);
		end

		if type=='cHTML'
		    ket_psi = strcat(ket_psi, '&gt;');
		else
		    ket_psi = strcat(ket_psi, '\rangle');
		end

		non_empty = 1;
	    end
	end
	if type=='cHTML'
            disp(strcat('<p>|&psi;<sub>', num2str(floor((j-1)/6)+1)-FROM_ZERO, num2str(mod(j-1,6)+1)-FROM_ZERO, '</sub>&gt; = ', ket_psi, '</p>'));
	else
            disp(strcat('$|\psi_{', num2str(floor((j-1)/6)+1)-FROM_ZERO, num2str(mod(j-1,6)+1)-FROM_ZERO, '}\rangle = ', ket_psi, '$'));
        end
%	disp('');
	
    end


end


%-------------------------------------------------------------------------------


function r=c2chess(c)
    chess_pieces = {'\kingB', '\queenB', '\knightB', '\bishopB', '\rookB', '\pawnB'};
    r = chess_pieces{floor((c-1) / 6)+1};
end



function r=c2color(c)
    chess_colors = {'red', 'cyan', 'green', 'magenta', 'blue', 'yellow'};
    r = chess_colors{mod(c-1,6)+1};

end


%-------------------------------------------------------------------------------


function U3colors(U,a,b,c)

    U3c=zeros(36);
    for j=1:36
    for k=1:36
        if abs(abs(U(j,k))-a) < 1e-10
            U3c(j,k) = 1;
        end
        
        if abs(abs(U(j,k))-b) < 1e-10
            U3c(j,k) = 2;
        end
        
        if abs(abs(U(j,k))-c) < 1e-10
            U3c(j,k) = 3;
        end
        
    end,end
    U3c
    imagesc(U3c)
end




%{

    example of output for >> officers('quhex')
    which is ready for TeX:

octave:236> officers('quhex')
$|\psi_{00}\rangle =c|10\rangle +a\omega^{3}|43\rangle +b|53\rangle$
$|\psi_{01}\rangle =c|00\rangle +b|43\rangle +a\omega^{7}|53\rangle$
$|\psi_{02}\rangle =c\omega^{17}|01\rangle +b|24\rangle +a\omega^{5}|34\rangle$
$|\psi_{03}\rangle =c\omega^{19}|11\rangle +a\omega^{5}|24\rangle +b|34\rangle$
$|\psi_{04}\rangle =b\omega^{14}|25\rangle +a\omega^{15}|35\rangle +a\omega^{18}|42\rangle +b\omega^{3}|52\rangle$
$|\psi_{05}\rangle =a\omega|25\rangle +b\omega^{12}|35\rangle +b\omega^{3}|42\rangle +a\omega^{18}|52\rangle$
$|\psi_{10}\rangle =c\omega^{10}|23\rangle +c\omega^{10}|50\rangle$
$|\psi_{11}\rangle =c\omega^{6}|33\rangle +c|40\rangle$
$|\psi_{12}\rangle =a\omega^{2}|04\rangle +b\omega^{5}|14\rangle +c\omega^{7}|41\rangle$
$|\psi_{13}\rangle =b\omega|04\rangle +a\omega^{14}|14\rangle +c\omega^{19}|51\rangle$
$|\psi_{14}\rangle =b\omega^{4}|05\rangle +a\omega^{9}|15\rangle +a\omega^{2}|22\rangle +b\omega^{13}|32\rangle$
$|\psi_{15}\rangle =a\omega^{3}|05\rangle +b\omega^{18}|15\rangle +b\omega^{19}|22\rangle +a|32\rangle$
$|\psi_{20}\rangle =c\omega^{2}|31\rangle +c\omega^{13}|44\rangle$
$|\psi_{21}\rangle =c\omega^{2}|21\rangle +c\omega^{7}|54\rangle$
$|\psi_{22}\rangle =c\omega^{19}|12\rangle +a\omega^{12}|45\rangle +b\omega|55\rangle$
$|\psi_{23}\rangle =c\omega^{5}|02\rangle +b\omega^{15}|45\rangle +a\omega^{14}|55\rangle$
$|\psi_{24}\rangle =a\omega|03\rangle +b\omega^{4}|13\rangle +c\omega^{8}|20\rangle$
$|\psi_{25}\rangle =b\omega^{10}|03\rangle +a\omega^{3}|13\rangle +c\omega^{16}|30\rangle$
$|\psi_{30}\rangle =b\omega^{10}|01\rangle +a\omega^{15}|11\rangle +a\omega^{4}|24\rangle +b\omega^{7}|34\rangle$
$|\psi_{31}\rangle =a\omega^{5}|01\rangle +b|11\rangle +b\omega^{17}|24\rangle +a\omega^{10}|34\rangle$
$|\psi_{32}\rangle =a|25\rangle +b\omega^{15}|35\rangle +b\omega^{14}|42\rangle +a\omega^{13}|52\rangle$
$|\psi_{33}\rangle =b\omega^{15}|25\rangle +a|35\rangle +a\omega^{7}|42\rangle +b\omega^{16}|52\rangle$
$|\psi_{34}\rangle =a\omega|00\rangle +b\omega^{16}|10\rangle +b\omega^{10}|43\rangle +a\omega^{5}|53\rangle$
$|\psi_{35}\rangle =b\omega^{14}|00\rangle +a\omega^{19}|10\rangle +a\omega^{5}|43\rangle +b\omega^{10}|53\rangle$
$|\psi_{40}\rangle =c|05\rangle +b\omega^{7}|22\rangle +a|32\rangle$
$|\psi_{41}\rangle =c|15\rangle +a\omega^{10}|22\rangle +b\omega^{13}|32\rangle$
$|\psi_{42}\rangle =c|23\rangle +c\omega^{10}|50\rangle$
$|\psi_{43}\rangle =c\omega^{10}|33\rangle +c\omega^{14}|40\rangle$
$|\psi_{44}\rangle =b\omega^{2}|04\rangle +a\omega^{15}|14\rangle +c\omega^{10}|51\rangle$
$|\psi_{45}\rangle =a\omega^{5}|04\rangle +b\omega^{8}|14\rangle +c|41\rangle$
$|\psi_{50}\rangle =a\omega^{10}|02\rangle +b\omega^{5}|12\rangle +b\omega^{9}|45\rangle +a\omega^{16}|55\rangle$
$|\psi_{51}\rangle =b\omega^{15}|02\rangle +a|12\rangle +a\omega^{16}|45\rangle +b\omega^{13}|55\rangle$
$|\psi_{52}\rangle =b\omega^{14}|03\rangle +a\omega^{7}|13\rangle +c\omega^{10}|30\rangle$
$|\psi_{53}\rangle =a\omega^{3}|03\rangle +b\omega^{6}|13\rangle +c|20\rangle$
$|\psi_{54}\rangle =c|31\rangle +c\omega|44\rangle$
$|\psi_{55}\rangle =c\omega^{16}|21\rangle +c\omega^{11}|54\rangle$


%}


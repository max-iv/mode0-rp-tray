library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity gateGen is
    Port ( clk : in STD_LOGIC;
           on_i : in STD_LOGIC;
           count_i : in STD_LOGIC_VECTOR (31 downto 0);
           startCount_i : in STD_LOGIC_VECTOR (31 downto 0);
           stopCount_i : in STD_LOGIC_VECTOR (31 downto 0);
           gate_o : out STD_LOGIC);
end gateGen;

architecture Behavioral of gateGen is
    signal gateSig : STD_LOGIC;
    begin
        process(clk)
            begin
                if rising_edge(clk) then
                    if on_i = '0' then
                        gateSig <= '0';
                    else
                        if UNSIGNED(startCount_i) < UNSIGNED(stopCount_i) then
                            if UNSIGNED(count_i) < UNSIGNED(startCount_i) then
                                gateSig <= '0';
                            else
                                if UNSIGNED(count_i) <= UNSIGNED(stopCount_i) then
                                    gateSig <= '1';
                                else
                                    gateSig <= '0';
                                end if;
                            end if;
                        else
                            gateSig <= '0';
                        end if;
                    end if;
                end if;
        end process;
        gate_o <= gateSig;
end Behavioral;

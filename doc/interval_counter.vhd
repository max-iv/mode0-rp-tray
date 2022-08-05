library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity interval_counter is
    Port ( clk : in STD_LOGIC;
           resetn : in STD_LOGIC;
           maxCount_i : in STD_LOGIC_VECTOR (31 downto 0);
           count_o : out STD_LOGIC_VECTOR (31 downto 0) );
end interval_counter;

architecture Behavioral of interval_counter is
    signal counter_reg : UNSIGNED (31 downto 0) := (others => '0');
    begin
        process(clk)
            begin
                if rising_edge(clk) then
                    if resetn = '1' then
                        counter_reg <= (others => '0');
                    else
                        if counter_reg >= UNSIGNED(maxCount_i) then
                            counter_reg <= (others => '0');
                        else
                            counter_reg <= counter_reg + 1;
                        end if;
                    end if;
                end if;
        end process;

        count_o <= STD_LOGIC_VECTOR(counter_reg);


end Behavioral;

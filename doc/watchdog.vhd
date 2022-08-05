library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity watchdog is
    Port ( clk : in STD_LOGIC;
           resetn : in STD_LOGIC;
           watchdog_o : out STD_LOGIC_VECTOR (31 downto 0));
end watchdog;

architecture Behavioral of watchdog is
    signal oneSecCounter_reg : UNSIGNED (31 downto 0) := (others => '0');
    signal watchdog_reg : UNSIGNED (31 downto 0) := (others => '0');

    begin
        process(clk)
            begin
                if rising_edge(clk) then
                    if resetn = '1' then
                        oneSecCounter_reg <= (others => '0');
                        watchdog_reg <= (others => '0');
                    else
                        if oneSecCounter_reg > 125000000 then
                            oneSecCounter_reg <= (others => '0');
                            watchdog_reg <= watchdog_reg + 1;
                            if watchdog_reg > 32760 then
                                watchdog_reg <= (others => '0');
                            end if;
                        else
                            oneSecCounter_reg <= oneSecCounter_reg + 1;
                        end if;
                    end if;
                end if;
        end process;
        watchdog_o <= STD_LOGIC_VECTOR(watchdog_reg);


end Behavioral;
